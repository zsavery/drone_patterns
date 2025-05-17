from typing import TypeVar

T = TypeVar('T')


def binary_search(lst: list, item: T) -> T:
    """
    Split the sorted list in half and search for the number.
    Use the midpoint as the pivot.

    :param lst: Sorted list
    :param item: instance to search for
    :return:  an item if found, else -1
    """
    # Base case: empty list
    if not lst:
        return -1

    # Base case: single element
    if len(lst) == 1:
        return lst[0] if lst[0] == item else -1

    # Find the midpoint
    mid = len(lst) // 2

    # Base case: found the item
    if lst[mid] == item:
        return lst[mid]

    # Recursive case: search left half if item is smaller
    if item < lst[mid]:
        return binary_search(lst[:mid], item)

    # Recursive case: search right half if the item is larger
    return binary_search(lst[mid + 1:], item)
