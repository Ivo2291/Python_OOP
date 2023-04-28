def squares(number):
    num = 1

    while num <= number:
        yield pow(num, 2)

        num += 1


print(list(squares(5)))
