class DictionaryIter:
    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())
        self.number = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == len(self.dictionary) - 1:
            raise StopIteration

        self.number += 1

        return self.dictionary[self.number]


result = DictionaryIter({"name": "Peter", "age": 24})
for x in result:
    print(x)
