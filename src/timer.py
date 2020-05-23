from time import time


class Timer:
    @staticmethod
    def init():
        __class__.prev_time = time()

    @staticmethod
    def capture_time():
        prev_time = __class__.prev_time
        current_time = time()
        __class__.elapsed_time = current_time - prev_time
        __class__.prev_time = current_time

    @staticmethod
    def get_elapsed():
        return __class__.elapsed_time

    prev_time = 0.0
    elapsed_time = 0.0
