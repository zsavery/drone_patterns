from binarry_search import binary_search
from random import randint
import pytest



@pytest.fixture
def sorted_list():
    test_lst = [7, 14, 17, 37, 53, 71, 82, 84, 90, 99]
    return test_lst
        


def test_empty_lst():
    test_lst = []
    assert len(test_lst) == 0, f"Expected lsit of size 0: {len(test_lst)}"
    assert test_lst == [], f"Expected empty list : {test_lst}"
    

    
def test_search_item_in_list(sorted_list):
    for i, v in enumerate(sorted_list):
        assert binary_search(sorted_list, sorted_list[i]) == v , f"Expected {sorted_list[i]} but got {binary_search(sorted_list, sorted_list[i])}"
    assert len(sorted_list) == 10 , f"List should have 10 elements, but has {len(sorted_list)}"

def test_search_item_not_in_list():
    
    pass