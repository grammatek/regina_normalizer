from regina_normalizer import unicode_normalizer as un
from regina_normalizer import dict_data

def test_unicode_norm():
    text = "text to norma\u00adlize"
    normalized = un.normalize_encoding(text)
    assert normalized == 'text to normalize'
    text = "Sinfóníu\u00a0hljómsveit"
    normalized = un.normalize_encoding(text)
    assert normalized == "Sinfóníu hljómsveit"
    text = "123 \u20ac"
    normalized = un.normalize_encoding(text)
    assert normalized == "123 \u20ac"

def test_post_norm_replacements():
    dict_data.PronDict('../regina_normalizer/data/lexicon.txt')
    print("dict len: " + str(len(dict_data.PronDict.get_lexicon())))
    text = "Jahrzehnte saß"
    normalized = un.normalize_alphabet(text)
    assert normalized[0] == "jahrsehnte sass"
    text = "( test ) #"
    normalized = un.normalize_alphabet(text)
    assert normalized[0] == ", test ,"
    text = "coventry"
    normalized = un.normalize_alphabet(text)
    assert normalized[0] == "coventry"
    text = "coventri"
    normalized = un.normalize_alphabet(text)
    assert normalized[0] == "koventri"
