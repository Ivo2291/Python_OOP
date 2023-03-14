class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False

        return True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


stack = Stack()
stack.push("Ivo")
stack.push("Ivo again")
stack.push('Hello')
print(stack.pop())
print(stack.top())
print(stack.is_empty())
print(stack.__str__())