def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def iterative_fibonacci(n):
    """
    1,1,2,3,5,8

    """
    if n < 0:
        return -1
    x,y = 0, 1

    # y, x = x+y, y
    for _ in range(n):
        y, x = x + y, y

    return y

if __name__ == '__main__':
    n_terms = 0 # nth number in a fibonacci sequence

    while True:
        n_terms = int(input("Number of terms: "))
        # check if the number of terms is valid
        if n_terms > 0:
            break
        else:
            print("Invalid input ! Please input a positive value")

    fibonacci_version = "None"


    result = None
    while fibonacci_version == "None":
        fibonacci_version = input(f"Fibonacci version\n1. Series\n2. Recursive\n3. Exit\nEnter your choice: ")
        match fibonacci_version.lower():
            case "series":
                result = iterative_fibonacci(n_terms)
                break
            case "recursive":
                result = recursive_fibonacci(n_terms)
                break
            case "exit"|"quit"|"q":
                break
            case _:
                fibonacci_version = "None"

    print(f"Fibonacci version: {fibonacci_version}\n" +
          f"Fibonacci nth term: {result}\n")

