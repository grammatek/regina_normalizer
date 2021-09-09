#!/usr/bin/env python3

import sys
from pos_tagger import POSTagger
from regina_normalizer import abbr_functions as af
from regina_normalizer import number_functions as nf


class Normalizer:

    def __init__(self):
        self.tagger = POSTagger.get_tagger()

    def normalize(self, sent, domain):
	    sent = af.replace_abbreviations(sent, domain)
	    sent = nf.handle_sentence(sent, domain, self.tagger)
	    print(sent)


def main():
    input = sys.argv[1]
    domain = sys.argv[2]
    normalizer = Normalizer()
    normalizer.normalize(input, domain)


if __name__ == '__main__':
    main()