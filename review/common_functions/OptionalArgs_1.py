# A demo of optional function arguments
def square(x=2):
    """
    Return the square of x.

    Arg:
        x: integer or float number w/ default value is 2
    Return:
        square of x; int if x is int, float if x is float
    """

    return x * x

def walk(distance=10) -> None:
    total_distance = square(distance)
    print(f"Walked {total_distance} meters")


if __name__ == '__main__':

    print(square())
    print(type(square()))

    print(square(8))
    print(type(square(8)))

    print(square(2.5))
    print(type(square(2.5)))

    walk()
    walk(5)

    """
    TypeError
    NoneType
    ArgumentError:
    
    """




