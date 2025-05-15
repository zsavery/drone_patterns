def check_item_off_lst(lst: list)-> str:
    """
    Get user input and reference list. If the user input matches the list item,
    remove the item from the list.
    :param lst: list
    :return: response: str
    """
    response = ""

    # prompt user and get user input
    response = input("Enter to-do item to complete or 'quit' to exit: ")

    # reference list
    for item in lst:
        if item.lower() == response.lower():
            response = item

    # remove item from list if user input matches list item
    if response in lst:
        lst.remove(response)

    # return user input
    return response

if __name__ == '__main__':
    todo_lst = [] # initialize an empty list

    # Prompt the user and get items for a to-do list
    print("Welcome to the to-do list program!")

    # add items until user enters quit
    response = "" # empty string for loop condition
    while response != "quit":
        # get user input
        response = input("Enter to-do item or 'quit' to exit: ")
        # add item to the list if the use does not enter quit
        if response != "quit":
            todo_lst.append(response)
        print(f"Current to-do list size: {len(todo_lst)}")
        # print("Current to-do list size: {}".format(len(todo_lst)))

    # use function to remove items from the list
    response = ""
    while response != "quit":
        print("Current to-do list: {}".format(todo_lst))
        response = check_item_off_lst(todo_lst)