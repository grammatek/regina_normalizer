"""
 This class holds different maps, containing unicode character encodings and their respective
 replacement for the unicode cleaning of raw text see unicode_normalizer.
 The maps are by no means finalized, need to be extended and adjusted, as we run into problematic
 characters.
"""

delete_chars_map = {
    '\u0000': "",  # <control> NULL
    '\u0001': "",  # <control> start of heading
    '\u0002': "",  # <control> start of text
    '\u0004': "",  # <control> end of transmission
    '\u0005': "",  # <control> enquiry
    '\u0006': "",  # <control> acknowledge
    '\u0008': "",  # <control> backspace
    '\u0010': "",  # <control> data link escape
    '\u0011': "",  # <control> device control one
    '\u0012': "",  # <control> device control two
    '\u0013': "",  # <control> device control three
    '\u0014': "",  # <control> device control four
    '\u0015': "",  # negative acknowledge
    '\u0016': "",  # synchronous idle
    '\u0017': "",  # end of transmission block
    '\u0018': "",  # cancel
    '\u0019': "",  # end of medium
    '\u001a': "",  # substitute
    '\u001b': "",  # escape
    '\u001f': "",  # unit separator
    '\u000e': "",  # shift out
    '\u000f': "",  # shift in
    '\u0098': "",  # start of string
    '\u00ad': "",  # soft hyphen
    '\u00d7': "",  # multiplication sign -> why delete?
    '\u02c8': "",  # modifier letter vertical line e.g. as stress mark in IPA
    '\u02cc': "",  # modifier letter low vertical line e.g. as secondary stress mark in IPA
    '\u200e': "",  # left-to-right mark
    # '\u2019': "",  # right single quotation mark -> why delete? moved to otherSubstMap
    '\ufeff': ""  # zero width no-break space
}

insert_space_map = {
    '\u0003': " ",  # <control> end of text
    '\u0007': " ",  # <control> bell
    '\u0009': " ",  # <control> horizontal tabulation
    '\u000b': " ",  # <control> vertical tabulation
    '\u000c': " ",  # <control> form feed
    '\u0080': " ",  # <control>
    '\u0081': " ",  # <control>
    '\u0082': " ",  # break permitted here
    '\u0095': " ",  # message waiting
    '\u00a0': " ",  # no-break space
    '\u200b': " ",  # zero width space
    '\u2028': " ",  # line spearator
    '\u2192': " ",  # rightwards arrow
    '\u220f': " ",  # n-ary product -> why delete?
    '\ufa07': " "  # ideograph spokes of wheel CJK -> check this range, CJK
}

# delete for now, transliterate later if necessary
ipa_map = {
    '\u0252': "",  # latin small letter turned alpha
    '\u0259': "",  # latin small letter schwa
    '\u0283': "",  # latin small letter esh
    '\u028a': "",  # latin small letter upsilon
    '\u028b': ""  # latin small letter v with hook
}

greek_alphabet = {
    '\u0394': "delta",  # greek capital letter delta
    '\u039b': "lambda",  # greek capital letter lambda
    '\u03a3': "sigma",  # greek capital letter sigma
    '\u03a4': "tá",  # greek capital letter tau
    '\u03ac': "alpha",  # greek small letter alpha with tonos
    '\u03ae': "eta",  # greek small letter eta with tonos
    '\u03af': "jóta",  # greek small letter iota with tonos
    '\u03b1': "alpha",  # greek small letter alpha
    '\u03b3': "gamma",  # greek small letter gamma
    '\u03b4': "delta",  # greek small letter delta
    '\u03b5': "epsilon",  # greek small letter epsilon. Subst with 'e'?
    '\u03b7': "eta",  # greek small letter eta
    '\u03b9': "jóta",  # greek small letter iota
    '\u03ba': "kappa",  # greek small letter kappa
    '\u03bb': "lambda",  # greek small letter lambda
    '\u03bc': "mu",  # greek small letter mu. Better subst.?
    '\u03bd': "nu",  # greek small letter nu. Better subst.?
    '\u03bf': "omicron",  # greek small letter omicron
    '\u03c0': "pí",  # greek small letter pi
    '\u03c1': "ró",  # greek small letter rho
    '\u03c2': "sigma",  # greek small letter final sigma. Better subst.?
    '\u03c3': "sigma",  # greek small letter sigma
    '\u03c4': "tá",  # greek small letter tau
    '\u03c5': "upsilon",  # greek small letter upsilon
    '\u03c6': "fí",  # greek small letter phi
    '\u03c7': "hjí",  # greek small letter chi. Better subst.?
    '\u03c9': "omega",  # greek small letter omega
    '\u03cc': "omicron",  # greek small letter omicron with tonos
    '\u03cd': "upsilon",  # greek small letter upsilon with tonos
    '\u1f00': "alpha",  # greek small letter alpha with psili
    '\u1f08': "alpha",  # greek capital letter alpha with psili
    '\u1fc6': "eta",  # greek capital letter eta with perispomeni
}

arabic_alphabet = {
    '\u0627': "",  # arabic letter alef
    '\u062f': "",  # arabic letter dal
    '\u0631': "",  # arabic letter reh
    '\u0641': "",  # arabic letter feh
    '\u0648': "",  # arabic letter waw
}

hebrew_alphabet = {
    '\u05d3': "",  # hebrew letter dalet
    '\u05d4': "",  # hebrew letter he
    '\u05d5': "",  # hebrew letter vav
    '\u05d9': "",  # hebrew letter yod
    '\u05db': "",  # hebrew letter kaf
    '\u05dc': "",  # hebrew letter lamed
    '\u05de': "",  # hebrew letter mem
    '\u05df': "",  # hebrew letter final nun
    '\u05e2': "",  # hebrew letter ayin
    '\u05e4': "",  # hebrew letter pe
    '\u05e7': "",  # hebrew letter qof
    '\u05e9': "",  # hebrew letter shin
    '\u05ea': "",  # hebrew letter taw
}

cyrillic_alphabet = {
    '\u0421': "",  # cyrillic capital letter es
    '\u0430': "",  # cyrillic small letter a
    '\u0438': "",  # cyrillic small letter i
    '\u043b': "",  # cyrillic small letter el
    '\u043d': "",  # cyrillic small letter en
    '\u043f': "",  # cyrillic small letter letter pe
    '\u0440': "",  # cyrillic capital letter er
    '\u0442': "",  # cyrillic small letter te
}

diverse_substitutions = {
    '\u0085': "...",  # next line (nel) -> why this substitution?
    '\u0091': "'",  # private use one -> why this substitution?
    '\u0092': "’",  # private use two -> why this substitution?
    '\u0096': "-",  # start of guarded area -> why this substitution?
    '\u00b4': "'",  # acute accent
    '\u2010': "-",  # hyphen
    '\u2011': "-",  # non-breaking hyphen
    '\u2012': "-",  # figure dash
    '\u2013': "-",  # en dash
    '\u2014': "-",  # em dash
    '\u2019': "'",  # right single quotation mark
    '\u201a': ",",  # single low-9 quotation mark
    '\u201c': "\"",  # left double qoutation mark
    '\u201d': "\"",  # right double qoutation mark
    '\u201e': "\"",  # double low-9 qoutation mark
    '\u201f': "\"",  # double high-reversed-9 qoutation mark
    '\u2212': "-",  # minus sign
    '\u2713': "-",  # check mark -> why this substitution?
    '\u0100': "A",  # latin capital letter A with macron (long a)
    '\u0101': "a",  # latin small letter a with macron (long a)
    '\u0106': "Ts",  # latin capital letter C with acute
    '\u0107': "ts",  # latin small letter c with acute
    '\u010c': "Tj",  # latin capital letter C with caron (similar to 'ch' in 'chocolate')
    '\u010d': "tj",  # latin small letter c with caron
    '\u0110': "Ð",  # latin capital letter D with stroke
    '\u0111': "ð",  # latin small letter d with stroke
    '\u0112': "E",  # latin capital letter E with macron
    '\u0113': "e",  # latin small letter e with macron
    '\u011b': "É",  # latin capital letter E with caron, /jE/
    '\u011c': "é",  # latin small letter e with caron, /jE/
    '\u011e': "G",  # latin capital letter G with breve -> note: should be pronunced /G/ SAMPA
    '\u011f': "g",  # latin small letter g with breve -> note: should be pronunced /G/ SAMPA
    '\u0131': "i",  # dotless i
    '\u0141': "Ú",  # latin capital letter L with stroke -> should resemble /w/, rather use 'L' subst?
    '\u0142': "ú",  # latin small letter l with stroke -> should resemble /w/, rather use 'l' subst?
    '\u0143': "Nj",  # latin capital letter N with acute
    '\u0144': "nj",  # latin small letter n with acute
    '\u0147': "Nj",  # latin capital letter N with caron
    '\u0148': "nj",  # latin small letter n with caron
    '\u014c': "O",  # latin capital letter O with macron
    '\u014d': "o",  # latin small letter o with macron
    '\u0152': "E",  # latin ligature OE
    '\u0153': "e",  # latin ligature oe
    '\u0158': "Hr",  # latin capital letter R with caron -> voiceless r
    '\u0159': "hr",  # latin small letter r with caron -> voiceless r
    '\u015e': "Sj",  # latin capital letter S with cedilla -> like German 'sch'
    '\u015f': "sj",  # latin small letter s with cedilla -> like German 'sch'
    '\u0160': "S",  # latin capital letter S with caron -> like 'sh' in 'she'
    '\u0161': "s",  # latin small letter s with caron -> like 'sh' in 'she'
    '\u016a': "Ú",  # latin capital letter U with macron
    '\u016b': "ú",  # latin small letter u with macron
    '\u0179': "S",  # latin capital letter Z with acute
    '\u017a': "s",  # latin small letter z with acute
    '\u017b': "S",  # latin capital letter Z with dot above
    '\u017c': "s",  # latin small letter z with dot above
    '\u0219': "s",  # latin small letter s with comma below
    '\u2032': "fet",  # prime -> add a sign for normalizer, that an inflection might be needed? fet, feta, ...
}

# merges all replacement dictionaries for simpler look up (does not contain the delete dictionary):
unified_dictionary = {**insert_space_map, **diverse_substitutions, **arabic_alphabet, **greek_alphabet,
                      **hebrew_alphabet, **cyrillic_alphabet, **ipa_map}

# if those characters are found in normalized words not contained in the pronunciation dictionary,
# we need to replace them with characters from the Icelandic alphabet
post_dict_lookup = {
    'c': "k",  # TODO: can we contextualize this?
    'w': "v",
    'z': "s",
    'q': "k",
    'å': "o",
    'ä': "e",
    'ü': "u",
    'ø': "ö",
    'ć': "ts",  # polish
    'ę': "e",
    'ł': "ú",  # polish, like English 'w' in 'will'
    'ń': "n",
    'ś': "s",
    'ß': "ss",
    'ź': "s",
    'ż': "s",
    'C': "K",  # TODO: can we contextualize this?
    'W': "V",
    'Z': "S",
    'Q': "K",
    'Å': "O",
    'Ä': "E",
    'Ü': "U",
    'Ø': "Ö",
}

characters_out_of_range_to_keep = [
    '\u20a4',  # Lira sign
    '\u20ac'  # Euro sign
]

combining_grave_accent = '\u0300'  # ̀
combining_acute_accent = '\u0301'  # ´ as in á,é, ...
combining_circumflex_accent = '\u0302'  # ̂
combining_tilde = '\u0303'  # ̃
combining_macron = '\u0304'  # ̄
combining_overline = '\u0305'  # ̅
combining_breve = '\u0306'  # ̆
combining_dot_above = '\u0307'  # ̇
combining_diaeresis = '\u0308'  # ¨ as in ä, ü, ...
# etc. upto u0362 all kinds of "combining" characters
