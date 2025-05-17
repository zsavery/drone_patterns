# Use timeit to measure the execution time
import cProfile
from count_by_var import count_by_var

cProfile.run("count_by_var(2, 1000)",)

