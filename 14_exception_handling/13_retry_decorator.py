import functools
import time

def retry(times=3, exceptions=(Exception,), delay=0.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"  attempt {attempt}/{times} failed: {e}")
                    if attempt == times:
                        raise                          # out of attempts: let the real error out
                    time.sleep(delay)
        return wrapper
    return decorator

calls = {"n": 0}

@retry(times=3, exceptions=(ConnectionError,))
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("network down")
    return "success"

print("flaky:", flaky())

@retry(times=2, exceptions=(ConnectionError,))
def always_down():
    raise ConnectionError("still down")

try:
    always_down()
except ConnectionError as e:
    print("gave up:", e)

@retry(times=3, exceptions=(ConnectionError,))
def wrong_kind():
    raise ValueError("a bug, not a network problem")

try:
    wrong_kind()
except ValueError as e:
    print("not retried:", e)