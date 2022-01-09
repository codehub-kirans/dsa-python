class Stack:
    """A Stack class"""
    def __init__(self) -> None:
        self.data=[]

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def inspect(self):
        return self.data[-1]

    def isEmpty(self):
        if self.data:
            return False
        else:
            return True


#Reverse a string using Stack
def reverseString(string):

    stack = Stack()
    for char in string:
        stack.push(char)

    while stack.isEmpty() is False:
        print(stack.pop(), end='')
    print()

reverseString("abcde")