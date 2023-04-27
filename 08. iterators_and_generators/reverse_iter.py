class ReverseIter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:
            raise StopIteration

        return self.iterable.pop()


reversed_list = ReverseIter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
