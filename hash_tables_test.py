from hash_tables import get_symmetric_pairs

def test_get_symmetric_pairs():
    pairs = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]
    assert get_symmetric_pairs(pairs) == [[30, 40], [5, 10]]


def test_get_symmetric_pairs_strings():
    pairs = [["Dan", "Kari"], ["Jeremy", "Val"], ["Jeremy", "Charles"], [
        "Devin", "Susan"], ["Kari", "Dan"], ["Devin", "Susan"]]
    assert get_symmetric_pairs(pairs) == [["Dan", "Kari"]]



def test_get_symmetric_pairs_no_pairs():
    pairs = [["Dan", "Kari"], ["Lisa", "Val"], ["Jeremy", "Charles"],
             ["Devin", "Susan"], ["Charles", "Jamie"]]
    assert get_symmetric_pairs(pairs) == []