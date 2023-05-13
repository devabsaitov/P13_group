# decorator

# 1 step
import time


def add_nums(n1, n2):
    return n1 + n2


res = add_nums
print(res(1, 3))


# 2 step

def hello():
    return "Hello world"


def add_nums(*args: tuple[str]):
    return sum(args)


def my_function(func):
    return func(1, 2, 3, 4)


print(my_function(add_nums))


# 3 step

def decorator(func):
    def inner():
        return func()

    return inner


def test():
    return "Hi"


print(decorator(test)())


# 4 step


def multiple(num):
    def wrapper(func):
        def inner(num3):

            # print("inner function")
            result = num * num3
            return func(result)
        return inner
    return wrapper



time.time()

@time_func
def lyboy_func(n):
    pass

print(lyboy_func(20))



