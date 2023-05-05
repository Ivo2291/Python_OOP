def make_bold(function):
    def wrapper(*args):
        res = function(*args)
        return f"<b>{res}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*args):
        res = function(*args)
        return f"<i>{res}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*args):
        res = function(*args)
        return f"<u>{res}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
print(greet("Peter"))
