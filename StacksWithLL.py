class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    def __repr__(self):
        return f"{self.val}"

class LinkedList:
    def __init__(self):
        self.head = None

    def show_items(self):
        curr_node=self.head
        while curr_node != None:
            print(f"{curr_node}-->",end="")
            curr_node=curr_node.next
        print("None")

class Stack(LinkedList):
    def push(self, val):
        curr_node=self.head
        if curr_node == None:
            self.head = Node(val)
        else:
            while curr_node.next != None:
                curr_node=curr_node.next
            curr_node.next=Node(val)
    def pop(self):
        pass

    def peek(self):
        pass


stack=Stack()
stack.push(56)
stack.push(644)
stack.show_items()

