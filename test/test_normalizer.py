from regina_normalizer import main as norm


def test_normalize():
    text = "Það voru e.t.v. 54 km eftir."
    normalizer = norm.Normalizer()
    normalized = normalizer.normalize(text, '')
    assert normalized == 'Það voru ef til vill  fimmtíu og fjórir kílómetrar eftir .'


def get_tuple_list():
    res_list = []
    tuple_list = [('Það', 'Það'), ('voru', 'voru'), ('e.t.v.', 'ef til vill'), ('54', ' fimmtíu og fjórir'),
                  ('km', 'kílómetrar'), ('eftir', 'eftir'), ('.', '.')]
    res_list.append(tuple_list)
    return res_list


def test_normalize_tokenwise():
    text = "Það voru e.t.v. 54 km eftir."
    normalizer = norm.Normalizer()
    normalized = normalizer.normalize_tokenwise(text, '')
    assert normalized == get_tuple_list()

