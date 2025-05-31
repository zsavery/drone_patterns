def recursive_fibonacci(n):
    print(f"recursive_fibonacci({n})")

def iterative_fibonacci(n):
    print(f"iterative_fibonacci({n})")


if __name__ == '__main__':

    # Change this to be user input if you wish!
    n_terms = 0

    while True:
        n_terms = int(input("Number of terms: "))
        # check if the number of terms is valid
        if n_terms > 0:
            break
        else:
            print("Invalid input ! Please input a positive value")

    fibonacci_version = "None"


    while fibonacci_version == "None":
        fibonacci_version = input(f"Fibonacci version\n1. Series\n2. Recursive\n3. Exit\nEnter your choice: ")
        match fibonacci_version.lower():
            case "series":
                recursive_fibonacci(n_terms)
                break
            case "recursive":
                iterative_fibonacci(n_terms)
                break
            case "exit"|"quit"|"q":
                break
            case _:
                fibonacci_version = "None"
