class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.height += 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.height -= 1
            return temp


