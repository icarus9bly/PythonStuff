class Node:
    def __init__(self, val):
        self.val = val
        self.next= None
        self.pre = None
    def __repr__(self):
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

    def insert(self, index, val):
        curr_node=self.head
        counter=1
        if index == 1:
            self.prepend(val)
        else:
            while counter < index:
                curr_node=curr_node.next
                counter+=1
            temp=curr_node.pre
            temp.next=Node(val)
            new_node=temp.next
            new_node.pre=temp
            new_node.next=curr_node
            curr_node.pre=new_node

    def remove(self, index):
        curr_node=self.head
        counter = 1
        while counter < index:
            curr_node = curr_node.next
            counter+=1
        temp=curr_node.next
        curr_node.pre.next=temp
        temp.pre=curr_node.pre

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
db_ll.insert(4,444)
db_ll.show_items()
db_ll.remove(4)
db_ll.show_items()