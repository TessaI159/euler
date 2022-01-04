import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self, times=1):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        average_elapsed_time = elapsed_time / times
        if times != 1:
            print(f"Average elapsed time: {average_elapsed_time:0.6f} seconds")
            print(f"Total elapsed time: {elapsed_time:0.6f} seconds")
        else:
            print(f"Elapsed time: {elapsed_time:0.6f} seconds")

    def time(self, function, *args):
        self.start()
        ret = function(*args)
        print(ret)
        self.stop()

    def time_multiple(self, function, times, *args):
        self.start()
        for x in range(times - 1):
            function(*args)
        print(function(*args))
        self.stop(times)
        
