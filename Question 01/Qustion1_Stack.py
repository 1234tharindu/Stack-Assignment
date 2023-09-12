import numpy  # import numpy library


class Stack:  # create Stack class
    def __init__(self, limit=5):  # Add limit
        self.limit = limit
        self.Stack = numpy.array([], int)  # numpy array assign self.Stack

    def push(self, data):  # push value to Stack
        if self.Stack.size < self.limit:  # check limit less than Stack.size
            self.Stack = numpy.append(self.Stack, [data])  # append data to stack
            return self.Stack
        else:
            print("Stack is overflow")

    def pop(self):  # pop function
        if len(self.Stack) == 0:  # check self.Stack equql to 0
            print("Stack is overflow")
        else:
            element = int(self.Stack[len(self.Stack) - 1])
            self.Stack = numpy.delete(self.Stack, -1)
            return element

    def top(self):  # top function
        if len(self.Stack) == 0:  # check len of self.Stack
            print("Stack is underflow")
        else:
            return self.Stack[len(self.Stack) - 1]

    def isEmptyStack(self):  # check is it empty or not  empty Stack
        return len(self.Stack) == 0

    def isfullStack(self):  # check is it full Stack
        return len(self.Stack) == self.limit

    def size(self):  # check Stack Size
        return len(self.Stack)
