import tracemalloc
from time import perf_counter

def time_and_memory_decorator(func):

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        answer = func(*args, **kwargs)
        end_time = perf_counter()
        current, peak = tracemalloc.get_traced_memory()

        print(f'{answer}')
        print(f'Peak memory use: {peak / 10**6:0.6f} MB')
        print(f'Time to execute: {end_time - start_time:0.6f}')
        tracemalloc.stop()

    return wrapper
