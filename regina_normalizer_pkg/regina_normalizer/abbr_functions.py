import re
import difflib
from typing import Tuple
import json
import os

from . import abbr_dict as abd 
from . import area_dict as ad
from . import currency_dict as cd
from . import denominator_dict as dend
from . import direction_dict as dird
from . import distance_dict as dd
from . import electronic_dict as ed
from . import period_dict as pd
from . import rest_dict as rd
from . import time_dict as td
from . import volume_dict as vd
from . import weight_dict as wd
from . import pre_help_dicts as phd
from . import symbols_dict as sd

direction_ptrn = "[SN]?V|N|[SN]?A|S"

pre_help_dict = phd.pre_help_dicts
abbr_dict = abd.abbr_dict
area_dict = ad.make_area_dict()
currency_dict = cd.make_currency_dict()
denominator_dict = dend.denominator_dict
direction_dict = dird.direction_dict
distance_dict = dd.make_distance_dict()
electronic_dict = ed.make_electronic_dict()
period_dict = pd.make_period_dict()
rest_dict = rd.make_rest_measure_dict()
time_dict = td.make_time_dict()
volume_dict = vd.make_volume_dict()
weight_dict = wd.make_weight_dict()
symb_dict = sd.symb_dict


def replace_in_list(token_list: list, token: str, replacement: str) -> list:
    """Replace all occurrences of 'token' with 'replacement' in the 'token_list'"""
    return [replacement if item == token else item for item in token_list]


def get_replacement(orig_text: str, replacement_text: str) -> Tuple[str, str]:
    """ Find the difference between the two input strings and extract the corresponding tokens.
    Return both tokens. """
    diff = difflib.ndiff(orig_text.split(' '), replacement_text.split(' '))
    to_replace = ''
    replacement = ''
    for d in diff:
        if d.startswith('-'):
            to_replace = d.split(' ')[1]
        elif d.startswith('+'):
            replacement = d.split(' ')[1]
    return to_replace, replacement


def replace_all(text: str, dic: dict, ptrn="") -> list:
    """ Replace words according to the appropriate dictionary.
    Return a list of tuples, containing original tokens and replacements."""

    original_list = text.split(' ')
    replaced_list = text.split(' ')
    zipped_result = zip(original_list, replaced_list)
    if re.findall(ptrn, text):
        for i, j in dic.items():
            if re.findall(i, text):
                sub_text = re.sub(i, j, text)
                to_replace, replacement = get_replacement(text, sub_text)
                replaced_list = replace_in_list(replaced_list, to_replace, replacement)
                text = sub_text
        zipped_result = zip(original_list, replaced_list)
    result_list = list(zipped_result)
    return replaced_list


# replace words according to the appropriate domain 
def replace_domain(splitsent, domain, ptrn="\-|\–|\—"):
    finalstring = ""
    for i in range(len(splitsent)):
        try:
            if re.match("\d", splitsent[i-1]) and re.match(ptrn, splitsent[i]) and re.match("\d", splitsent[i+1]):
                if domain == 'sport':
                    splitsent[i] = ""
                else:
                    splitsent[i] = "til"
        except:
            pass
        finalstring += splitsent[i] + " "
    #return finalstring
    return splitsent

def replace_abbreviations(sent, domain):
    original_list = sent.split(' ')
    sent_list = replace_all(sent, direction_dict, direction_ptrn)
    sent_list = replace_all(' '.join(sent_list), pre_help_dict)
    sent_list = replace_all(' '.join(sent_list), denominator_dict, "\/")
    sent_list = replace_all(' '.join(sent_list), weight_dict, wd.weight_ptrn)
    sent_list = replace_all(' '.join(sent_list), distance_dict, dd.distance_ptrn)
    sent_list = replace_all(' '.join(sent_list), area_dict, ad.area_ptrn)
    sent_list = replace_all(' '.join(sent_list), volume_dict, vd.volume_ptrn)
    sent_list = replace_all(' '.join(sent_list), time_dict, td.time_ptrn)
    sent_list = replace_all(' '.join(sent_list), currency_dict, cd.currency_ptrn)
    sent_list = replace_all(' '.join(sent_list), electronic_dict, ed.electronic_ptrn)
    sent_list = replace_all(' '.join(sent_list), rest_dict, rd.rest_ptrn)
    sent_list = replace_all(' '.join(sent_list), period_dict, pd.period_ptrn)
    sent_list = replace_all(' '.join(sent_list), abbr_dict)
    sent_list = replace_domain(sent_list, domain)
    return list(zip(original_list, sent_list))

