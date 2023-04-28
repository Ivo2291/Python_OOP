class CountdownIterator:
    def __init__(self, count: int):
        self.count = count
        self.iterations = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration

        self.iterations += 1

        return self.count - self.iterations


iterator = CountdownIterator(10)
for item in iterator:
    print(item, end=" ")
