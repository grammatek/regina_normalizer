import logging
from pathlib import Path
class PronDict:

    lexicon = None

    def __init__(self, lexicon_file='data/lexicon.txt'):
        """
        Initialize the lexicon containing the words from the pronunciation dictionary
        :param lexicon_file: path to lexicon file
        """
        try:
            with open(lexicon_file) as f:
                PronDict.lexicon = f.read().splitlines()
        except OSError:
            PronDict.lexicon = []
            logging.error("Could not read lexicon file: " + lexicon_file)

    @staticmethod
    def get_lexicon():
        if PronDict.lexicon is None:
            PronDict()
        return PronDict.lexicon