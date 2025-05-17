from binary_search import binary_search

def create_sorted_lists():
    """Create and return sorted lists of different types"""
    int_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    float_lst = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
    string_lst = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    return int_lst, float_lst, string_lst

def get_search_item(my_type):
    while True:
        try:
            value = input(f"Enter a {my_type} to search for or 'back' to change type: ")
            if value.lower() == 'back':
                return 'back'
            if my_type == int:
                return int(value)
            elif my_type == float:
                return float(value)
            else:
                return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {my_type}")

def search_type(type_name: str, lst: list, type_class):
    """Handle continuous searching for a specific type"""
    while True:
        search_item = get_search_item(type_class)
        if search_item == 'back':
            return None

        result = binary_search(lst, search_item)
        if result == -1:
            print("Item not found in the list")
        else:
            print(f"Found: {result}")



if __name__ == "__main__":
    """Main program loop"""
    int_lst, float_lst, string_lst = create_sorted_lists()
    print("Make a type selection to select a list to search!")

    while True:
        response = input("\nEnter 'int', 'float', 'string' or 'quit' to exit: ").lower()

        match response:
            case "int":
                search_type("integer", int_lst, int)
            case "float":
                search_type("float", float_lst, float)
            case "string":
                search_type("string", string_lst, str)
            case "quit":
                print("Goodbye!")
                break
            case _:
                print("Invalid type selection!")
