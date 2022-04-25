from permutations import permutations
from hypothesis import given, strategies as st, assume
from math import factorial
from operator import mul
from functools import reduce

MAX_LENGTH = 9


def test_permutations_simple_string_in_set():
    string = 'abc'
    assert string in permutations(string)


@given(st.text())
def test_permutations_string_in_set(x):
    assert permutations('') == {}
    assume(x != '' and len(x) < MAX_LENGTH)
    assert x in permutations(x)


@given(st.text())
def test_permutations_length_set(x):
    assert len(permutations('')) == 0
    assume(x != '' and len(x) < MAX_LENGTH)
    unique = set(x)
    l1 = [x.count(char) for char in unique]
    l2 = [factorial(i) for i in l1]
    prod = reduce(mul, l2, 1)
    assert len(permutations(x)) == int(factorial(len(x))/prod)

# Unsure of how to conduct a permutation test
# @given(st.permutations(st.text()), st.text())
# def test_permutations_in_function(x, y):
#     z = permutations(y)
#     for val in x:
#         assert val in z
