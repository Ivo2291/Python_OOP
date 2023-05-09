def type_check(some_type):
    def decorator(function):
        def wrapper(arg):
            if not isinstance(arg, some_type):
                return "Bad Type"

            return function(arg)

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
