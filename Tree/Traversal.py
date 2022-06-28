
class Node:
    def __init__(self,data=0):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,data=0):
        self.root = Node(data)

    # -------------------------------- pre-Order ---------------------------
    # During the function calling we are not passing root node of tree, instead we are
    # dividing the traversal into two parts and passing root node of tree to another method
    # i.e., "inorderT"
    def inorderTraversal(self):
        self.inorderT(self.root)
        print()
    # Indirectly called by inorderTraversal method to print data passing root node
    def inorderT(self,root):
        if root is None:
            return
        self.inorderT(root.left)
        print(root.data, end=" ")
        self.inorderT(root.right)

    # -------------------------------- pre-Order ---------------------------

    def preorderTraversal(self):
        self.preorderT(self.root)
        print()

    # Indirectly called by preorderTraversal method to print data passing root node
    def preorderT(self,root):
        if root is None:
            return

        print(root.data, end=" ")
        self.preorderT(root.left)
        self.preorderT(root.right)

    # -------------------------------- post-Order ---------------------------
    def postorderTraversal(self):
        self.postorderT(self.root)
        print()

    # Indirectly called by postorderTraversal method to print data passing root node
    def postorderT(self,root):
        if root is None:
            return
        self.postorderT(root.left)
        self.postorderT(root.right)
        print(root.data, end=" ")

if __name__ == "__main__":

    bt = Tree()
    bt.root.data = 1
    bt.root.left,bt.root.right = Node(2), Node(3)
    leftChild = bt.root.left
    leftChild.left, leftChild.right = Node(4), Node(5)
    rightChild = bt.root.right
    rightChild.left, rightChild.right = Node(6), Node(7)

    # Calling inorderTraversal for the tree
    bt.inorderTraversal()
    # Calling preorderTraversal for the tree
    bt.preorderTraversal()
    # Calling postorderTraversal for the tree
    bt.postorderTraversal()
