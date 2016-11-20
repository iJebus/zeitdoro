from functools import update_wrapper
from api import start_api, stop_api


def api(f):
    def wrapper(*args, **kwargs):
        start_api()
        f()
        stop_api()
    return update_wrapper(wrapper, f)
