import json

if __name__ == '__main__':

    # Read the JSON file
    with open('my_list.json', 'r') as file:
        float_list = json.load(file)['unsorted_list']

    # Print the list of floats
    print(float_list)
    print(type(float_list))

    # Sort the list of floats
    sorted_list = [] # code here

    with open('sorted_list.json', 'w') as file:
        json.dump({'sorted_list': sorted_list}, file)