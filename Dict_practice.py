# Simple practice with a dictionary
if __name__ == '__main__':
    # Creating and empty dictionary
    myProfile = {}
    # Printing a dictionary
    #print(myProfile)

    # adding values to a dictionary
    myProfile = {"name": "Carter",
                 "age": 26,
                 "city": "Frisco",
                 "state": "Texas"}

    # Printing a dictionary (full)
    #print(myProfile)
    # Printing a dictionary (single value)
    #print(myProfile["age"])

    # Adding new key:value pair to a dictionary
    myProfile["job"] = "Curriculum Developer"
    myProfile['hobbies'] = ['fishing', 'programming', 'hiking']

    # Modifying existing key:value pairs
    myProfile["name"] = "Jason"
    myProfile['hobbies'].append('singing')

    print(myProfile)








