class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def printTree(self):
        temp = self.root
        
if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

