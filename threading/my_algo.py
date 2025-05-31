def selection_sort(lst: list)-> list:
 """
 Sort a list of floats using selection sort. Selection Sort divides the array into a
 sorted and an unsorted part. It repeatedly finds the minimum from the unsorted part
 and moves it to the sorted part.

 Complexity: O(n^2)
 Best case: O(n^2)
 Worst case: O(n^2)
 :param lst: list
 :return
 """
 result = lst
 for i in range(len(result)):
  min_index = i
  for j in range(i+1, len(result)):
   if result[min_index] > result[j]:
    min_index = j
  result[i], result[min_index] = result[min_index], result[i]
 return result


def bubble_sort(lst):
 """
 Sort a list of floats using bubble sort. Bubble Sort repeatedly steps through the
 list, compares adjacent elements, and swaps them if they are in the wrong order. This
 process repeats until no swaps are needed.

 Complexity: O(n^2)
 Best Case: O(n)
 Worst Case: O(n^2)

 """
 # Initialize the sorted list
 result = lst
 # Iterate over the list
 for i in range(len(result)):
  # Iterate over the unsorted list
  for j in range(i + 1, len(result)):
   # Swap if the element is greater than the next element
   if result[i] > result[j]:
    result[i], result[j] = result[j], result[i]
 return result

def binary_search(lst: list, item: int) -> int:
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

