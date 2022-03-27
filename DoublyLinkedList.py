class Node:
    def __init__(self, val):
        self.val = val
        self.next= None
        self.pre = None
    def __str__(self):
        return f"{self.val}"

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, val):
        curr_node=self.head
        if curr_node == None:
            """If Linked list is empty insert node as head."""
            self.head = Node(val)
        else:
            while curr_node.next != None:
                """Traverse till we reach the last node in the list which points to None not the actual node with is Node."""
                curr_node=curr_node.next
            curr_node.next=Node(val)
            curr_node.next.pre=curr_node

    def prepend(self, val):
        curr_node=self.head
        if curr_node == None:
            self.head = Node(val)
        else:
            temp = curr_node
            self.head = Node(val)
            self.head.next = temp
            temp.pre=self.head

    def show_items(self):
        curr_node=self.head
        while curr_node != None:
            print(f"{curr_node}<-->",end="")
            curr_node=curr_node.next
        print("None")

db_ll=DoublyLinkedList()
db_ll.append(56)
db_ll.append(111)
db_ll.append(909)
db_ll.append(775)
db_ll.show_items()
db_ll.prepend(789)
db_ll.show_items()