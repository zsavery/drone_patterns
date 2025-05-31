import cProfile
import multiprocessing
import random
import time
from my_algo import   bubble_sort
from my_algo import selection_sort


def profile_selection_sort(lst):
    # Enable profile for selection_sort
    pr = cProfile.Profile()
    # Enable profile
    pr.enable()
    # using a copy of our collection runit true
    selection_sort(lst.copy())
    # disable profile
    pr.disable()
    # print stats
    pr.print_stats()

def profile_bubble_sort(lst):
    # Enable profile for selection_sort
    pr = cProfile.Profile()
    # Enable profile
    pr.enable()
    # using a copy of our collection runit true
    bubble_sort(lst.copy())
    # disable profile
    pr.disable()
    # print stats
    pr.print_stats()

if __name__ == "__main__":
    # Generate a random sample array
    arr = [random.randint(0, 1000) for _ in range(1000)]

    # Run selection_sort and bubble_sort in parallel using multiprocessing
    p1 = multiprocessing.Process(target=profile_bubble_sort, args=(arr,)) # Edit line
    p2 = multiprocessing.Process(target=profile_selection_sort, args=(arr,)) # Edit Line

    # Do not change below
    start_time = time.time() # get time at start

    p1.start() # start process 1
    p2.start() # start process 2

    p1.join() # join process 1
    p2.join() # join process 2

    end_time = time.time() # get time at end

    print(f"Total elapsed time: {end_time - start_time:.4f} seconds")
