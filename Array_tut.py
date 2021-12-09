class MyArray():
    def __init__(self):
        self.length=0
        self.data=[]
    def get(self, index):
        return self.data[index]
    def __str__(self) -> str:
        return f'Data is {str(self.data)} and length of array {self.length}'
    def __repr__(self) -> str:
        return f'Data is {str(self.data)} and length of array {self.length}'
arr=MyArray()
print(arr)