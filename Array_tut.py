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
        for ix, num in enumerate(self.data):
            if ix >= index:
                self.data[index] = self.data[index+1]
        self.length -= 1
        return item
        # To be done

    def __str__(self) -> str:
        return f'Data is {str(self.data)} and length of array {self.length}'

    def __repr__(self) -> str:
        return f'MyArray()'


arr = MyArray()
arr.push(34)
arr.push(57585)
arr.push(57.890)
arr.push(89)
# arr.pop()
print(arr)
arr.delete(1)
print(arr)
