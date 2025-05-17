# Use timeit to measure the execution time
import timeit
from count_by_var import count_by_var


execution_time = timeit.timeit("count_by_var(3, 500)",
                               setup="from __main__ import count_by_var",
                               number=100)
print(f"Time: {execution_time:.6f}")

##########################################################
test_function = lambda: count_by_var(3, 500)

execution_time = timeit.timeit(test_function, number=100)
print(f"Time: {execution_time:.6f}")