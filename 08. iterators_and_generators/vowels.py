class vowels:
    def __init__(self, text: str):
        self.vowels_list = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
        self.text = [el for el in text if el in self.vowels_list]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.text:
            raise StopIteration

        return self.text.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
