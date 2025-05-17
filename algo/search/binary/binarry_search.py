from random import randint
from typing import T

# https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1

def binary_search(lst: list, num: T):
    """
    Split the sorted list in half and search for the number.
    Use the midpoint as the pivot.

    :param lst: sorted list
    :param num: int to search for
    :return: num if found, else -1
    """
    
    if len(lst) == 0:
        raise ValueError("List is empty")
    
    # find the midpoint of the list
    midpoint = len(lst) // 2

    # compare the number to the midpoint

    if num == lst[midpoint]:
        return lst[midpoint]

    # split list in half into new_lst
    new_lst = []
    
    if num < lst[midpoint]:
        # search left half
        new_lst = lst[:midpoint]
    else:
        # search right half
        new_lst = lst[midpoint:]
    # check if the new list is empty
    if len(new_lst) == 0:
        return -1

    # call binary search on the new list
    return binary_search(new_lst, num)



if __name__ == '__main__':

    lst_size = 16
    num_lst = []


    for i in range(lst_size):
        random_num = randint(0, 100)
        num_lst.append(random_num)
    num_lst.sort()
    print(num_lst)

    # use user input to get the number to search for
    num_to_find = int(input("Enter a number to search for: "))

    size = len(num_lst)

    midpoint = size // 2
    """
    / - divide
    // - divide and round down
    % - remainder
    """

    """
    [0, 2, 5, 7, 10, 22, 25, 27, 30, 32, 35]
                      m
    [5, 27, 30, 32, 35]
             m 
    [5, 27]
     m 
    [27]
      m
    []
    """

    binary_search(num_lst, num_to_find)