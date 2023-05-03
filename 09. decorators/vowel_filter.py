def vowel_filter(function):

    def wrapper():
        vowels = ["a", "e", "o", "u", "i", "y"]

        return [char for char in function() if char.lower() in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e", "f", "i", "u"]


print(get_letters())
