def recursive_factorial(n):
    if n <= 1:
        return n
    return recursive_factorial(n - 1) * n

if __name__ == '__main__':
    # Get
    num = 6

    # Call factorial
    print("Factorial of number", num, "=", recursive_factorial(num))
