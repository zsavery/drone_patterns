# Simple practice with a dictionary
if __name__ == '__main__':
    # Creating and empty dictionary
    myProfile = {}
    #my_profile_lst = []
    # Printing a dictionary
    print(myProfile)

    # adding values to a dictionary
    myProfile = {"name": "Carter",
                 "age": 26,
                 "city": "Frisco",
                 "state": "Texas"}

    #my_profile_lst = ["Carter", 26, "Frisco", "Texas"]

    # Printing a dictionary (full)
    print(myProfile)
    # print(my_profile_arr)
    # Printing a dictionary (single value)
    print(myProfile["age"])
    # print(my_profile_arr[1])

    # Adding new key:value pair to a dictionary
    myProfile["age"] = 20
    # my_profile_lst[1] = 34
    myProfile["job"] = "Curriculum Developer"
    # my_profile_lst.append("Nun")
    myProfile['hobbies'] = ['fishing', 'programming', 'hiking']
    # my_profile_lst.append(['fishing', 'programming', 'hiking'])

    # Modifying existing key:value pairs
    myProfile["name"] = "Jason"
    myProfile['hobbies'].append('singing')

    print(myProfile)








