class SequenceRepeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.iterations = - 1
        self.counter = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.number - 1:
            raise StopIteration

        self.iterations += 1

        if self.counter == len(self.sequence) - 1:
            self.counter = - 1

        self.counter += 1

        return self.sequence[self.counter]


result = SequenceRepeat('I Love Python', 3)
for item in result:
    print(item, end='')
