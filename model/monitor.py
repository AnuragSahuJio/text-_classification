
from functools import wraps

import time


def monitor_prediction_time():

    """

    Decorator to monitor the time taken for predictions.

    """

    def decorator(func):

        @wraps(func)

        def wrapper(*args, **kwargs):

            start_time = time.time()

            result = func(*args, **kwargs)

            end_time = time.time()

            print(f"Prediction time: {end_time - start_time:.2f} seconds")

            return result

        return wrapper

    return decorator


