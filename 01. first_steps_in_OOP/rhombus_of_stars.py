def print_output_row():
    print(" " * (number - row), end="")
    for i in range(1, row + 1):
        print("* ", end="")
    print()


number = int(input("Enter a number: "))

for row in range(1, number + 1):
    print_output_row()

for row in range(number - 1, -1, -1):
    print_output_row()
