# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree
class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)


# create root
root = Tree(1)
''' following is the tree after above statement
		1
	/ \
	None None'''

root.left = Tree(2)
root.right = Tree(3)

''' 2 and 3 become left and right children of 1
		1
		/ \
		2	 3
	/ \ / \
None None None None'''


root.left.left = Tree(4)
'''4 becomes left child of 2
		1
	   / \
	  /   \
	 2	   3
    / \    /\
   /   \  /  \
  4 None None None
 / \
None None'''

# rootNonOOP = [1, [2, [4, None, None], None], [3, None, None]]

print(f'Top root node val: {root.val}')


# iteratively
def inorder_traversal_iter(root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right


# Recursively
res = []

root2 = Tree(5)
root2.right = Tree(3)


def inorder_traversal_recurse(root):
    if root:
        inorder_traversal_recurse(root.left)
        res.append(root.val)
        inorder_traversal_recurse(root.right)
    return res


print(inorder_traversal_iter(root))
print(inorder_traversal_recurse(root2))