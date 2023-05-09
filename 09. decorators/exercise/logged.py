def logged(function):
    def wrapper(*args):
        res = f'you called {function.__name__}{args}'

        result = res + '\n' + f'it returned {function(*args)}'

        return result

    return wrapper


@logged
def sum_func(a, b):
    return a + b


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
print(sum_func(1, 4))
