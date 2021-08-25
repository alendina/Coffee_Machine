class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
