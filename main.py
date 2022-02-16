# content of test_expectation.py
import pytest


import pytest

def test_tuple_is_unchangable():
    try:
        tuple = (1, 2, 3)
        tuple[1] = 2
        assert False
    except TypeError:
        pass
@pytest.mark.parametrize("n,expected", [((1, (1,2), [1]), (1, (1,2), [1])), ((), ())])
def test_tuple_init(n, expected):
    tuple = (n)
    assert tuple == expected

@pytest.mark.parametrize("n,expected", [(3, 2), ('notExistInTuple', 0), ((1, 3, 'apple', 3, 'apple'), 1), ((1, 3, 'apple', 3, 'apple', (1, 3, 'apple', 3, 'apple')), 0)])
def test_tuple_count(n, expected):
    tuple = (1, 3, 'apple', 3, 'apple', (1, 3, 'apple', 3, 'apple'))
    assert tuple.count(n) == expected

@pytest.mark.parametrize("n,expected", [(3, 1), ((1, 3, 'apple', 3, 'apple'), 5)])
def test_tuple_index(n, expected):
    tuple = (1, 3, 'apple', 3, 'apple', (1, 3, 'apple', 3, 'apple'))
    assert tuple.index(n) == expected

def test_tuple_index_notExisting():
    tuple = (1, 3, 'apple', 3, 'apple', (1, 3, 'apple', 3, 'apple'))
    try:
        tuple.index('notExist')
        assert False
    except ValueError:
        pass


@pytest.mark.parametrize("n, expected", [('key', 'value'), ((1,2), ([1,2,3]))])
def test_dictionary_happy_pass(n, expected):
    dict = {'key': 'value', (1, 2): [1, 2, 3]}
    assert dict.get('key') == 'value'
    assert dict.get((1,2)) == [1, 2, 3]

def test_dictionarty_with_mutable_key():
    try:
        dict = {[1,2,3]: 'value', (1, 2): [1, 2, 3]}
        assert False
    except TypeError:
        pass

def test_dictionary_with_several_keys_return_last():
        dict = {'key': 'value', 'key': [1, 2, 3]}
        assert dict.get('key') == [1, 2, 3]

