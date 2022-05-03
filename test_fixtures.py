import pytest

@pytest.fixture
def empty_list():
    return []

@pytest.fixture
def one_item(empty_list):
    empty_list.append("item")
    return empty_list

@pytest.fixture
def so_fancy():
    fancy_object = FancyObject()

    yield fancy_object

    fancy_object.cleanup()

class FancyObject:
    def __init__(self):
        self.fancy = True
        print(f"\nFancyObject: {self.fancy}")

    def or_is_it(self):
        self.fancy = not self.fancy

    def cleanup(self):
        print(f"\ncleanup: {self.fancy}")

def test_len_of_empty_list(empty_list): # pytest matches empty_list from @pytest.fixture
    assert isinstance(empty_list, list)
    assert len(empty_list) == 0


def test_len_of_unary_list(one_item):
    assert isinstance(one_item, list) # passes in the function one_item()
    assert len(one_item) == 1
    assert one_item[0] == "item"

def test_so_fancy(so_fancy):
    assert so_fancy.fancy
    so_fancy.or_is_it()
    assert not so_fancy.fancy