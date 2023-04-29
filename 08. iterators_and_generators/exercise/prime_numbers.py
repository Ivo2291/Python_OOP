def get_primes(numbers):

    for number in numbers:
        if number > 1:
            number_is_prime = True

            for num in range(2, number):
                if number % num == 0:
                    number_is_prime = False
                    break

            if number_is_prime:
                yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
