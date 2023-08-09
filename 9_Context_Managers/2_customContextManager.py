class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        print(f"Time elapsed: {self.end_time - self.start_time} seconds")

with Timer():
    time.sleep(2)
