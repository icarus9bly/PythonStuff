# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head != None:
            curr_node=self.head
            while curr_node.next != None:
                curr_node=curr_node.next
                # print(curr_node)
            curr_node.next=Node(val)
        else:
            self.head=Node(val)

    def preprend(self, val):
        if self.head != None:
            curr_elem=self.head
            self.head=Node(val)
            self.head.next=curr_elem
        else:
            self.head=Node(val)

    def get_element(self,index):
        idx=1
        current_node=self.head
        while current_node.next != None:
            if idx == index:
                return current_node.data
            current_node=current_node.next
            idx+=1
        return None



    def list_elements(self):
        elems=[]
        cursor=self.head
        while cursor != None:
            print(cursor)
            elems.append(cursor)
            cursor=cursor.next
            
        


if __name__=="__main__":
    node1=Node(67)
    node2=Node(33)
    node3=Node(6447)
    node4=Node(67444)
    # print(node1.data,node2.data,node3.data,node4.data)
    myLinkedList= LinkedList()
    myLinkedList.head=node1
    myLinkedList.head.next=node2
    myLinkedList.head.next.next=node3
    myLinkedList.head.next.next.next=node4
    myLinkedList.append(77767889)
    print(f'{myLinkedList.head.data}-->{myLinkedList.head.next.data}-->{myLinkedList.head.next.next.data}-->{myLinkedList.head.next.next.next.data}-->{myLinkedList.head.next.next.next.next.data}')
    myLinkedList.preprend("11111")
    myLinkedList.list_elements()
    # print("-"*100)
    print(myLinkedList.get_element(1))
