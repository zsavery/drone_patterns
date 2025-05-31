import json
def bubble_sort(lst):
    """Sort a list of floats using bubble sort. Bubble Sort repeatedly steps through the
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


if __name__ == '__main__':
    # Read the text file
    with open('my_list.txt', 'r') as file:
        float_list = [float(line.strip()) for line in file]

    # Print the list of floats
    print(float_list)

    # Sort the list of floats
    sorted_list = bubble_sort(float_list) # code here

    # Print sorted list
    print(sorted_list)

    with open('sorted_list.txt', 'w') as file:
        for item in sorted_list:
            file.write(f"{item}\n")
