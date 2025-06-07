from timeit import timeit

def power_of(n=0, b=2):
    """
    Calculate the power of a number using recursive approach.
    
    Args:
        n (int): The exponent (power to raise to). Defaults to 0.
        b (int): The base number. Defaults to 2.
    
    Returns:
        int: The result of b raised to the power of n (b^n)
    
    Examples:
        >>> power_of(3, 2)
        8
        >>> power_of(0, 2)
        1
        >>> power_of(2)  # using default base=2
        4
    """
    if n == 0:
        return 1
    return power_of(n-1, b) * b


def power_of_lib(n, b=2, lib=None):
    """
    Calculate the power of a number using recursive approach with memoization.
    
    Args:
        n (int): The exponent (power to raise to).
        b (int): The base number. Defaults to 2.
        lib (dict): Dictionary to store previously calculated values for memoization.
                   Defaults to None and creates empty dict if not provided.
    
    Returns:
        int: The result of b raised to the power of n (b^n)
    
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> power_of_lib(3, 2)
        8
        >>> power_of_lib(0)
        1
        >>> power_of_lib(2, 3)  # 3^2
        9
        >>> power_of_lib(-1)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        ValueError: n must be positive
    """
    if n < 0:
        raise ValueError('n must be positive')
    if lib is None:
        lib = {}
    if n in lib:
        return lib[n]
    if n == 0:
        lib[n] = 1
        return 1
    lib[n] = power_of_lib(n - 1, b, lib) * b
    return lib[n]


if __name__ == '__main__':
    # Dictionary to store memoized values
    power_dict = {}

    # Test parameters
    nth_term = 12
    base = 2

    # Measure execution time of the regular recursive function
    execute_time = timeit(lambda: power_of(nth_term, base), number=1000)
    print(f"Time taken for power_of: {execute_time:.6f} seconds")

    # Measure execution time of the memoized recursive function
    execute_time_lib = timeit(lambda: power_of_lib(nth_term, base), number=1000)
    print(f"Time taken for power_of_lib: {execute_time_lib:.6f} seconds")
