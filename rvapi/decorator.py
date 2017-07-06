
import pyrvapi


def rvapi_flush(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        pyrvapi.rvapi_flush()
    return wrapper

