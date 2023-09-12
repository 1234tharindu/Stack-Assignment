class Node:  # create Node class
    def __init__(self, data):  # create init
        self.data = data
        self.next = None


class Stack:  # create class Stack
    def __init__(self, limit=5):  # Add limit
        self.size = 0  # assign value
        self.head = None
        self.limit = limit

    def push(self, data):  # create push function & pass self ,data parameter
        if self.size < self.limit:  # check size less than self.limit
            NewNode = Node(data)  # create new node & set the new data as the new node
            NewNode.next = self.head
            self.head = NewNode
            self.size += 1  # size must increase

        else:
            x = "Stack over flow"
            return x

    def isEmptyStack(self):  # This function check stack empty or not empty
        return self.size == 0  # if self.size equal to 0 return true or false

    def pop(self):  # pop function
        if self.isEmptyStack():  # if  statement false return x
            x = " Stack underflow "
            return x

        else:
            del_Node = self.head  # equal head to del_node
            self.head = self.head.next  # assign the head.next to self.head
            del_Node.next = None  # if del_node'next value equal None
            self.size -= 1  # one of value Reduction the size
            return del_Node.data

    def top(self):  # top function
        if self.isEmptyStack():  # check is stack empty
            return None  # if empty Stack return None
        else:
            return self.head.data  # is condition false return head.data

    def size_stack(self):  # check Stack size
        return self.size

    def isfullStack(self):  # check Stack is full or no
        return self.size == self.limit  # if limit equal to size return true .if  else return false
