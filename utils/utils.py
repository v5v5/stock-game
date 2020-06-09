import time

class Measure:
    time_start = 0

    def __init__(self):
        pass

    @staticmethod
    def start():
        Measure.time_start = time.time()
    
    @staticmethod
    def get():
        return time.time() - Measure.time_start
