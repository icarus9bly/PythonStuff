# Reverse this string using Array:
# "Hi my name is Aditya" to "aytidA si eman iH"
# from ..Array_tut import MyArray
class MyArray():
    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data.append(item)
        self.length += 1

    def pop(self):
        self.last_item = self.data[-1]
        self.data = self.data[0:-1]
        self.length -= 1
        return self.last_item

    def delete(self, index):
        # Delete the item at index and shift the items from to the left
        item = self.data[index]
        for ix in range(len(self.data)):
            if ix >= index and ix < self.length-1:
                self.data[ix] = self.data[ix+1]
        self.pop()
        return item
    def __str__(self) -> str:
        return f'Data is {str(self.data)} and length of array {self.length}'

    def __repr__(self) -> str:
        return f'MyArray()'

def reverse(data):
    arr= MyArray()
    rev=[]
    # Push whole string in the Array
    for char in data:
        arr.push(char)
    # Iterate over arr data and pop elems from it and also push that into reversed array. At last join all elems into a string    
    for elem in arr.data:
        rev.append(arr.pop())
    return ''.join(rev)

print(reverse("Hi my name is Aditya"))