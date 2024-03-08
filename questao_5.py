class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    
def invert(s : str) -> str:
    stack = Stack()
    for c in s:
        stack.push(c)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result

print(invert("hello")) # olleh