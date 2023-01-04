#!/usr/bin/env python3

import sys
import argparse
import re
import difflib

from tokenizer import Tokenizer
from regina_normalizer import pos_tagger
from regina_normalizer import dict_data
from regina_normalizer import abbr_functions as af
from regina_normalizer import number_functions as nf
from regina_normalizer import unicode_normalizer as un


class Normalizer:
    """
    The Normalizer as an interface to regina normalizer offers two methods: one that returns a normalized version
    of an input string as string, and one that returns a list of tuples, preserving  the original tokens mapped
    to their normalized representation.
    """

    def __init__(self):
        self.tokenizer = Tokenizer()
        self.tagger = pos_tagger.POSTagger.get_tagger()
        self.pron_dict = dict_data.PronDict.get_lexicon()

    def extract_prenorm_tuples(self, prenorm_sent, sent):
        """
        Find changes in prenorm_sent compared to sent and create tuples with original token and expanded abbreviation
        Example:
        sent == Það voru t.d. 5 atriði
        prenorm_sent == Það voru til dæmis 5 atriði

        return [('Það', 'Það'), ('voru', 'voru'), ('t.d.', 'til dæmis'), ('5', '5), ('atriði', 'atriði')]
        :param prenorm_sent:
        :param sent:
        :return:
        """
        norm_tuples = []
        prenorm_arr = prenorm_sent.split()
        sent_arr = sent.split()

        diff = difflib.ndiff(sent_arr, prenorm_arr)
        # a token from sent_arr not occurring in the prenorm_arr, store while processing the same/near positions in prenorm_arr
        current_key = ''
        # a token from prenorm_arr not occurring in the sent_arr, store while processing the same/near positions in sent_arr
        current_value = ''

        for elem in diff:
            if elem[0] == ' ':
                if current_key and current_value:
                    # add the orignal (key) - prenorm (value) tuple to the results
                    norm_tuples.append((current_key.strip(), current_value.strip()))
                    current_key = ''
                    current_value = ''
                norm_tuples.append((elem[2:], elem[2:]))
            elif elem[0] == '-':
                # elem in list1 but not in list2
                current_key += ' ' + str(elem[2:])
            elif elem[0] == '+':
                # elem in list2 but not in list1
                current_value += ' ' + str(elem[2:])
        if current_key and current_value:
            norm_tuples.append((current_key.strip(), current_value.strip()))
        return norm_tuples


    def merge_tuples_old(self, norm_tuples, pre_tuples):
        """
        Make sure the resulting tuple list contains the final version of the normalization as well as the original
        tokens. The 'pre_tuples' contains all original tokens but possibly not the final normalization. On the other hand,
        'norm_tuples' contains the final normalization, but not necessarily correctly organized in tuples compared
        to the original tokens, since the input to the second step of normalization already contains expanded
        abbreviations.
        We can not be absolutely sure that the both tuple lists correspond, the normalizer might have done errors at
        some stage. That's why we need to do a careful comparison to definitely have the original tokens plus the final
        normalization (correct or not) in the final tuple list.

        Example of an erroneous input (the pre normalization added a '5' in the wrong place - this bug is fixed but there might be more ...):
        pre_tuples: [('Miðaverð', 'Miðaverð'), ('fyrir', 'fyrir'), ('fullorðna'), ('fullorðna'), ('kr.', '5 krónur'), ('5500', '5500')]
        norm_tuples: [('Miðaverð', 'Miðaverð'), ('fyrir', 'fyrir'), ('fullorðna'), ('fullorðna'), ('5', 'fimm'), ('krónur', 'krónur'),
            ('5500', 'fimm þúsund og fimm hundruð')]

        desired output:
        [('Miðaverð', 'Miðaverð'), ('fyrir', 'fyrir'), ('fullorðna'), ('fullorðna'), ('kr.', 'fimm krónur'),
            ('5500', 'fimm þúsund og fimm hundruð')]

        :param norm_tuples: result of second step of normalization (handle_sentence_tokenwise())
        :param pre_tuples: result of first step of normalization (replace_abbreviations())
        :return: a list of tuples where first elem of each tuple represents an original token and the second elem the
        final normalized version of that token
        """
        final_tuples = []
        j = 0
        max_j = len(norm_tuples) - 1
        for i in range(len(pre_tuples)):
            if j > max_j:
                final_tuples.append(pre_tuples[i])
            elif norm_tuples[j][0] == pre_tuples[i][0]:
                # equal pre normalized, norm_tuple is valid
                final_tuples.append(norm_tuples[j])
            else:
                # norm_tuple contains an expansion as first elem, e.g. 'ef' from 'ef til vill' instead of 'e.t.v.'
                # we also have to deal with potential errors, store next original token from pre-normalized and find
                # the corresponding token in the normalized tuple list
                if i < len(pre_tuples) - 1:
                    next_original = pre_tuples[i + 1][0]
                else:
                    next_original = pre_tuples[i][0]
                norm_expanded = norm_tuples[j][1]
                while j < max_j and norm_tuples[j + 1][0] != next_original:
                    j += 1
                    norm_expanded += ' ' + norm_tuples[j][1]
                final_tuples.append((pre_tuples[i][0], norm_expanded))
            j += 1
        return final_tuples

    def merge_tuples(self, norm_tuples, pre_tuples):
        """
        Make sure the resulting tuple list contains the final version of the normalization as well as the original
        tokens. The 'pre_tuples' contains all original tokens but possibly not the final normalization. On the other hand,
        'norm_tuples' contains the final normalization, but not necessarily correctly organized in tuples compared
        to the original tokens, since the input to the second step of normalization already contains expanded
        abbreviations.
        We can not be absolutely sure that the both tuple lists correspond, the normalizer might have done errors at
        some stage. That's why we need to do a careful comparison to definitely have the original tokens plus the final
        normalization (correct or not) in the final tuple list.

        Example of an erroneous input (the pre normalization added a '5' in the wrong place - this bug is fixed but there might be more ...):
        pre_tuples: [('Miðaverð', 'Miðaverð'), ('fyrir', 'fyrir'), ('fullorðna', 'fullorðna'), ('kr.', '5 krónur'), ('5500', '5500')]
        norm_tuples: [('Miðaverð', 'Miðaverð'), ('fyrir', 'fyrir'), ('fullorðna', 'fullorðna'), ('5', 'fimm'), ('krónur', 'krónur'),
            ('5500', 'fimm þúsund og fimm hundruð')]

        desired output:
        [('Miðaverð', 'Miðaverð'), ('fyrir', 'fyrir'), ('fullorðna', 'fullorðna'), ('kr.', 'fimm krónur'),
            ('5500', 'fimm þúsund og fimm hundruð')]

        :param norm_tuples: result of second step of normalization (handle_sentence_tokenwise())
        :param pre_tuples: result of first step of normalization (replace_abbreviations())
        :return: a list of tuples where first elem of each tuple represents an original token and the second elem the
        final normalized version of that token
        """
        final_tuples = []

        j = 0
        max_j = len(norm_tuples) - 1
        for i in range(len(pre_tuples)):
            if j > max_j:
                final_tuples.append(pre_tuples[i])
            elif norm_tuples[j][0] == pre_tuples[i][0]:
                # equal pre normalized, norm_tuple is valid
                final_tuples.append(norm_tuples[j])
            else:
                # norm_tuple contains an expansion as first elem, e.g. 'ef' from 'ef til vill' instead of 'e.t.v.'
                # we also have to deal with potential errors, store next original token from pre-normalized and find
                # the corresponding token in the normalized tuple list
                if i < len(pre_tuples) - 1:
                    next_original = pre_tuples[i + 1][0]
                else:
                    next_original = pre_tuples[i][0]
                norm_expanded = norm_tuples[j][1]
                while j < max_j and norm_tuples[j + 1][0] != next_original:
                    j += 1
                    norm_expanded += ' ' + norm_tuples[j][1]
                final_tuples.append((pre_tuples[i][0], norm_expanded))
            j += 1
        return final_tuples

    def normalize(self, text, domain=''):
        """
        Normalizes input, taking domain into account ('sport' or '')
        Example:
        text: 'Það voru e.t.v. 55 km eftir. Þannig fór nú það.'
        returns: [['Það voru ef til vill fimmtíu og fimm kílómetrar eftir .'], ['Þannig fór nú það .']]

        :param text: text to normalize
        :param domain: domain to take into account, 'sport' causes a special handling of hyphens
        :return: normalized version of text
        """
        res = []
        for sent in self.tokenizer.detect_sentences(text):
            sent = af.replace_abbreviations(sent, domain)
            normalized = nf.handle_sentence(sent, domain, self.tagger).strip()
            final_sent = un.normalize_alphabet(normalized)
            res.append(final_sent)

        return res

    def normalize_tokenwise(self, text, domain):
        """
        This method returns a list of list of tuples where each tuple contains the original token from 'text' and the
        normalized version of the token, and each list represents one sentence.

        Example:
        input: 'Það voru e.t.v. 54 km eftir. Þannig fór nú það.'
        returns: [[('Það', 'Það'), ('voru', 'voru'), ('e.t.v.', 'ef til vill'), ('55', 'fimmtíu og fjórir'),
        ('km', 'kílómetrar), ('eftir', 'eftir), ('.', '.')], [('Þannig', 'Þannig'), ('fór', 'fór'), ('nú', 'nú'),
        ('það', 'það'), ('.', '.')]]

        :param text:
        :param domain:
        :return:
        """
        res = []

        for sent in self.tokenizer.detect_sentences(text):
            # first step is to replace abbreviations
            prenorm_sent = af.replace_abbreviations(sent, domain)
            # normalized_tuples contain the final normalized sentence as the second element of each tuple
            normalized_tuples = nf.handle_sentence_tokenwise(prenorm_sent, domain, self.tagger)
            # if abbreviations were replaced in the first step, we need to process the tuples further
            if prenorm_sent != sent:
                prenorm_tuples = self.extract_prenorm_tuples(prenorm_sent, sent)
                normalized_tuples = self.merge_tuples(normalized_tuples, prenorm_tuples)

            normalized_tuples = un.normalize_alphabet_from_tuples(normalized_tuples)
            res.append(normalized_tuples)

        return res


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_text", help="a text to normalize")
    parser.add_argument("-d", "--domain", default="other", help="the domain of the input text, 'sport' or 'other'")
    parser.add_argument("-f", "--format", default="plain", help="the format of the output, 'plain' or 'tokens'")
    args = parser.parse_args()
    return args


def main():
    cmdline_args = parse_arguments()
    input_text = cmdline_args.input_text
    domain = cmdline_args.domain
    output_format = cmdline_args.format
    normalizer = Normalizer()
    if output_format == "plain":
        print(normalizer.normalize(input_text, domain))
    elif output_format == "tokens":
        print(normalizer.normalize_tokenwise(input_text, domain))


if __name__ == '__main__':
    main()