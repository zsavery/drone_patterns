import json


def selection_sort(lst: list)-> list:
    """
    Sort a list of floats using selection sort. Selection Sort divides the array into a
    sorted and an unsorted part. It repeatedly finds the minimum from the unsorted part
    and moves it to the sorted part.

    Complexity: O(n^2)
    Best case: O(n^2)
    Worst case: O(n^2)
    """
    result = lst
    for i in range(len(result)):
        min_index = i
        for j in range(i+1, len(result)):
            if result[min_index] > result[j]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result


if __name__ == '__main__':

    # Read the JSON file
    with open('my_list.json', 'r') as file:
        float_list = json.load(file)['unsorted_list']

    # Print the list of floats
    print(float_list)
    print(type(float_list))

    # Sort the list of floats
    sorted_list = selection_sort(float_list)

    # Print sorted list
    print(sorted_list)

    with open('sorted_list.json', 'w') as file:
        json.dump({'sorted_list': sorted_list}, file)