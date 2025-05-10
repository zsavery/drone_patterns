from random import randint
# https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1
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

    size = len(num_lst)

    midpoint = size // 2
    """
    / - divide
    // - divide and round down
    % - remainder
    """

    """
    [0, 2, 5, 7, 10, 22, 25, 27, 30, 32, 35]
                      m
    [5, 27, 30, 32, 35]
             m 
    [5, 27]
     m 
    [27]
      m
    []
    """