from Qustion1_Stack import Stack  # import Stack file to this file

mystack = Stack()  # Stack assign mystack variable

mystack.push(5)
mystack.push(10)
mystack.push(15)
mystack.push(20)
mystack.push(25)

print("pop value is - ", mystack.pop())

print("Top value is -", mystack.top())

print("Is this Stack Empty (True/false) - ", mystack.isEmptyStack())

print("Is this Stack fullStack (True/false) -", mystack.isfullStack())

print("How many element in this Stack -", mystack.size())
