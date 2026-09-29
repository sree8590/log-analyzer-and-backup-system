from functools import wraps


def log_execution(function):
    """Decorator that displays function start and completion."""

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"\nFunction started: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Function completed: {function.__name__}")

        return result

    return wrapper