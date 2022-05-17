class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    def __str__(self):
        # return f"{self.left.value}<--{self.value}-->{self.right.value}"
        return f"{self.value}"

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

root_node = Node(55)
bt = BinarySearchTree(root_node)
bt.root.left = Node(10)
bt.root.right = Node(60)

print(bt.root)
print(bt.root.left)
print(bt.root.right)

#############################################################################################################################

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    def __str__(self):
        return str(self.value)

root = TreeNode(100)
root.left=TreeNode(50)
root.right=TreeNode(70)

print(root)
print(root.left)
print(root.right)