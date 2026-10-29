import functools
import tracemalloc
from time import perf_counter


def time_and_memory_decorator(func=None, *, iterations=1, adaptive=False):
    """
    Measures peak memory and execution time.
    Execution time is benchmarked cleanly WITHOUT tracemalloc overhead.

    Can be used as:
      @time_and_memory_decorator
      @time_and_memory_decorator(iterations=100)
      @time_and_memory_decorator(adaptive=True)  # auto-tunes runs for fast funcs
    """
    if func is None:
        return lambda f: time_and_memory_decorator(
            f, iterations=iterations, adaptive=adaptive
        )

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Clean timing run WITHOUT tracemalloc
        t0 = perf_counter()
        answer = func(*args, **kwargs)
        first_time = perf_counter() - t0

        # Determine timing iterations
        runs = iterations
        if adaptive:
            if first_time > 0.05:
                runs = 1
            else:
                runs = max(1, min(1000, int(0.1 / max(first_time, 1e-6))))

        if runs > 1:
            times = [first_time]
            for _ in range(runs - 1):
                t0 = perf_counter()
                func(*args, **kwargs)
                times.append(perf_counter() - t0)
            exec_time = min(times)
        else:
            exec_time = first_time

        # 2. Separate memory run WITH tracemalloc (isolated from timing)
        tracemalloc.start()
        try:
            func(*args, **kwargs)
            _, peak = tracemalloc.get_traced_memory()
        finally:
            tracemalloc.stop()

        # Format outputs (keeps exact character compatibility with check_all.py)
        peak_str = f"Peak memory use: {peak / 10**6:0.6f} MB"
        time_str = f"Time to execute in seconds: {exec_time:0.6f}"

        return answer, peak_str, time_str

    return wrapper
