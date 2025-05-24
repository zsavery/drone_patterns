import json

if __name__ == '__main__':
    # Read the text file
    with open('my_list.txt', 'r') as file:
        float_list = [float(line.strip()) for line in file]

    # Print the list of floats
    print(float_list)

    # Sort the list of floats
    sorted_list = [] # code here

    with open('sorted_list.txt', 'w') as file:
        for item in sorted_list:
            file.write(f"{item}\n")
