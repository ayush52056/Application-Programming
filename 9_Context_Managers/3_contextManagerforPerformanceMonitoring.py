import time

class PerformanceMonitor:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        if execution_time > 1:
            print(f"Performance Alert: Execution time exceeded 1 second. Time: {execution_time:.2f} seconds.")
        else:
            print(f"Execution time: {execution_time:.2f} seconds")

with PerformanceMonitor():
    time.sleep(2)
