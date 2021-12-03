# class Node:
#     def __init__(self, data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         pass


class Stack:
    def __init__(self):
        self.items=[]
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)       
    def is_empty(self):
        return not self.items
    def __str__(self):
        return str(self.items)
def main():
    mysta=Stack()
    mysta.push(45)
    mysta.push(43434345)
    mysta.push(44)
    mysta.push(549)
    mysta.push(45)
    mysta.push(7788)
    mysta.push(44555)
    print(mysta)
    print(mysta.size())
    print(mysta.pop())
    print(mysta.peek())
    print(mysta.is_empty())
    print(mysta)

if __name__=="__main__":
    main()
