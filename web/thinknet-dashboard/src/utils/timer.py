import time

class Timer:
    """
    Utility for measuring execution durations.
    """

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self) -> float:
        if self.start_time is None:
            raise Exception("Timer was not started.")
        elapsed = time.time() - self.start_time
        self.start_time = None
        return elapsed
