from regina_normalizer import main as norm


def test_normalize():
    text = "Það voru e.t.v. 54 km eftir."
    normalizer = norm.Normalizer()
    normalized = normalizer.normalize(text, '')
    assert normalized == [['Það voru ef til vill  fimmtíu og fjórir kílómetrar eftir .']]


def get_tuple_list():
    res_list = []
    tuple_list1 = [('Það', 'Það'), ('voru', 'voru'), ('e.t.v.', 'ef til vill'), ('54', ' fimmtíu og fjórir'),
                  ('km', 'kílómetrar'), ('eftir', 'eftir'), ('.', '.')]
    tuple_list2 = [('Þannig', 'Þannig'), ('fór', 'fór'), ('nú', 'nú'), ('það', 'það'), ('.', '.')]
    res_list.append(tuple_list1)
    res_list.append(tuple_list2)
    return res_list


def test_normalize_tokenwise():
    text = "Það voru e.t.v. 54 km eftir. Þannig fór nú það."
    normalizer = norm.Normalizer()
    normalized = normalizer.normalize_tokenwise(text, '')
    assert normalized == get_tuple_list()

