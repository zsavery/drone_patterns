import pytest
from binarry_search import binary_search


def test_binary_search_basic():
    """Test basic binary search functionality"""
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(lst, 5) == 5
    assert binary_search(lst, 1) == 1
    assert binary_search(lst, 10) == 10


def test_binary_search_not_found():
    """Test when element is not in list"""
    lst = [1, 2, 3, 4, 5]
    assert binary_search(lst, 6) == -1
    assert binary_search(lst, 0) == -1
    assert binary_search(lst, -1) == -1


def test_binary_search_empty_list():
    """Test with empty list"""
    assert binary_search([], 1) == -1


def test_binary_search_single_element():
    """Test with a single element list"""
    assert binary_search([1], 1) == 1
    assert binary_search([1], 2) == -1


def test_binary_search_duplicate_elements():
    """Test with duplicate elements"""
    lst = [1, 2, 2, 2, 3, 4, 5]
    assert binary_search(lst, 2) == 2


def test_binary_search_large_numbers():
    """Test with large numbers"""
    lst = [1000, 2000, 3000, 4000, 5000]
    assert binary_search(lst, 3000) == 3000
    assert binary_search(lst, 6000) == -1


def test_binary_search_negative_numbers():
    """Test with negative numbers"""
    lst = [-5, -4, -3, -2, -1, 0, 1]
    assert binary_search(lst, -3) == -3
    assert binary_search(lst, 0) == 0
    assert binary_search(lst, -6) == -1


def test_binary_search_edge_cases():
    """Test edge cases"""
    lst = [1, 2]
    assert binary_search(lst, 1) == 1
    assert binary_search(lst, 2) == 2
    assert binary_search(lst, 3) == -1


def test_binary_search_floats():
    """Test with floating point numbers"""
    lst = [1.1, 2.2, 3.3, 4.4, 5.5]
    assert binary_search(lst, 3.3) == 3.3
    assert binary_search(lst, 2.5) == -1
