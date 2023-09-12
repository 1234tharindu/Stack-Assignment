from Qustion2_Stack import Stack

myStack = Stack()

print("How many element in this Stack", myStack.size_stack())

myStack.push(5)
myStack.push(10)
myStack.push(15)
myStack.push(20)
myStack.push(25)

print("Is this Stack Empty (True/false -)", myStack.isEmptyStack())

print("pop value is -", myStack.pop())

print("Top value is -", myStack.top())

print("Is this Stack fullStack (True/false -", myStack.isfullStack())

print("How many element in this Stack", myStack.size_stack())
