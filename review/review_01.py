def hello()-> None:
    print("Hello World!")

def hello_name(name: str)-> None:
    # print("Hello {}!".format(name))
    print(f"Hello {name}!")

if __name__ == '__main__':
    x = "Houston"
    print(x)

    x = 5
    print(x)
    print(type(x)) # outputs int

    x = 5.0
    print(x)
    print(type(x)) # outputs float

    x = 5
    y = 10
    """
    comparison bools
    equals ==
    not equals !=
    greater than >
    less than <
    greater than or equal to >=
    less than or equal to <=
    """
    print(x == y) # False
    print(x != y) # True
    print(x > y) # False
    print(x < y) # True
    print(x >= y)
    print(x <= y)
    print(type(x == y)) # outputs bool

    if (x == y):
        print("x is equal to y")
    else:
        print("x is not equal to y")
###################################
    if x == y:
        print("x is equal to y")
    elif y < 12:
        print("y is less than 12")
    elif y > 12:
        print("y is greater than 12")

    while x < 10: # when x is equal to 10, the loop will stop
        print(x)
        x += 1 # x = x + 1

    for i in range(10):
        print(i)

    hello()
    hello_name("Houston")