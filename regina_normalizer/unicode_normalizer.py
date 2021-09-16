from regina_normalizer import unicode_maps as um
"""
Handles Unicode cleaning and Unicode normalizing of text. To simplify further processing, text normalizeing and
grapheme-to-phoneme conversion, we clean the text of most unicode characters not contained in the Icelandic
alphabet, and also delete or substitue a number of punctuation characters and special symbols.
"""

# the Icelandic alphabet
CHAR_SET = ['a', 'á', 'b', 'd', 'ð', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'p', 'r',
            's', 't', 'u', 'ú', 'v', 'y', 'ý', 'þ', 'æ', 'ö', 'x']


def normalize_encoding(text):
    """ Normalize the unicode encoding of the input text. This includes deleting or substituting certain characters
    and symbols, as defined in unicode_maps"""
    normalized_text = text
    for c in text:
        repl = get_replacement(c)
        if repl is not None:
            normalized_text = normalized_text.replace(c, repl)
        if should_delete(c):
            normalized_text = normalized_text.replace(c, '')

    return normalized_text


def get_replacement(char):
    if char in um.unified_dictionary:
        return um.unified_dictionary[char]


def should_delete(char):
    return char in um.delete_chars_map


def main():
    text = 'norma\u00adlize this and \u0394'
    normalized = normalize_encoding(text)
    print(text)
    print(normalized)


if __name__ == '__main__':
    main()