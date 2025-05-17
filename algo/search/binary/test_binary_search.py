from binarry_search import binary_search
import pytest


@pytest.fixture
def sorted_list():
    """Fixture to provide a sorted list for testing."""
    return [7, 14, 17, 37, 53, 71, 82, 84, 90, 99]


def test_empty_list():
    """Test binary search with an empty list."""
    test_lst = []
    assert len(test_lst) == 0, f"Expected list of size 0, but got {len(test_lst)}"
    assert test_lst == [], f"Expected empty list, but got {test_lst}"
    with pytest.raises(ValueError):
        binary_search(test_lst, 1)


def test_search_item_in_list(sorted_list):
    """Test binary search for items that exist in the list."""
    for index, value in enumerate(sorted_list):
        expected_value = sorted_list[index]
        result = binary_search(sorted_list, value)
        assert result == expected_value, f"Expected {expected_value}, but got {result}"
    
    assert len(sorted_list) == 10, f"List should have 10 elements, but has {len(sorted_list)}"


def test_search_item_not_in_list(sorted_list):
    """Test binary search for items that do not exist in the list."""
    not_in_list = [1, 15, 50, 100]
    for value in not_in_list:
        result = binary_search(sorted_list, value)
        assert result == -1, f"Expected -1 for value {value}, but got {result}"