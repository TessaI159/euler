import tracemalloc
from time import perf_counter

def time_and_memory_decorator(func):

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        answer = func(*args, **kwargs)
        end_time = perf_counter()
        current, peak = tracemalloc.get_traced_memory()

        peak = f'Peak memory use: {peak / 10**6:0.6f} MB'
        time_to_ex = f'Time to execute in seconds: {end_time - start_time:0.6f}'
        
        tracemalloc.stop()
        
        return answer, peak, time_to_ex

    return wrapper
