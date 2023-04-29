from itertools import permutations


def possible_permutations(elements):
    for el in permutations(elements):
        yield list(el)

# second_solution

# def possible_permutations(elements):
#     length = len(elements)
#
#     if length <= 1:
#         yield elements
#
#     else:
#         for n in range(length):
#             for end in possible_permutations(elements[:n] + elements[n + 1:]):
#                 yield [elements[n]] + end
#


[print(n) for n in possible_permutations([1, 2, 3])]
print()
[print(n) for n in possible_permutations([1])]
