def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'


for char in my_generator():
    print(char)


def parent(num):
    # print("Printing from the parent() function")

    def first_child():
        # print("Printing from the first_child() function")
        return "Hi, I am Emma"

    def second_child():
        # print("Printing from the second_child() function")
        return "Call me Liam"

    # second_child()
    # first_child()

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
print(first())


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
say_whee()


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


import functools
import time


def timer(func):  #2
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):  #4
        start_time = time.perf_counter()
        value = func(
            *args, **kwargs
        )  #*args untuk 1 parameter timer(1) **kwargs untuk parameter tambahan timer(timer=1)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer  #3


@timer
def waste_some_time(num_times):  #2

    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(1)  #1
