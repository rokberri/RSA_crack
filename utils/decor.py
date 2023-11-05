
import time


def get_runtime(func):
    def wrapper(arg):
        start_time = time.monotonic()
        print(func(arg))
        print('Время выполнения: ', time.monotonic() - start_time)

    return wrapper