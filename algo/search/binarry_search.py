from random import randint

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