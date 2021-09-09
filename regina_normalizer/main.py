#!/usr/bin/env python3

import sys

from tokenizer import split_into_sentences
from regina_normalizer import pos_tagger
from regina_normalizer import abbr_functions as af
from regina_normalizer import number_functions as nf


class Normalizer:

    def __init__(self):
        self.tagger = pos_tagger.POSTagger.get_tagger()

    def normalize(self, input, domain):
        res = ''
        for sent in split_into_sentences(input):
            sent = af.replace_abbreviations(sent, domain)
            res += ' ' + nf.handle_sentence(sent, domain, self.tagger)

        return res.strip()


def main():
    input = sys.argv[1]
    domain = sys.argv[2]
    normalizer = Normalizer()
    print(normalizer.normalize(input, domain))


if __name__ == '__main__':
    main()