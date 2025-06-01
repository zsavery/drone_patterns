from timeit import timeit

def power_of(n=0, b=2):
    if n == 0:
        return 1
    return power_of(n-1, b) * b


def power_of_lib(n, b=2, lib=None):
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
    power_dict = {}
    nth_term = 12
    base = 2
    func = lambda : power_of(nth_term, base)
    func_lib = lambda : power_of_lib(nth_term, base, power_dict)

    try:
        execute_time = timeit(func ,number=1000)
        print('execute time: {0:.8f} seconds.'.format(execute_time))
    except ValueError as e:
        print(e)

    try:
        execute_time = timeit(func_lib ,number=1000)
        print(f'execute time: {execute_time:.8f} seconds.')
    except ValueError as e:
        print(e)