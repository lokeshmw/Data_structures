class Node:

    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, t_root, e):
        temp = None
        while t_root:
            temp = t_root
            if e == t_root.element:
                return
            elif e < t_root.element:
                t_root = t_root.left
            elif e > t_root.element:
                t_root = t_root.right
        n = Node(e)
        if self.root:
            if e < temp.element:
                temp.left = n
            else:
                temp.right = n
        else:
            self.root = n

    def search(self, key):
        t_root = self.root
        while t_root:
            if key == t_root.element:
                return True
            elif key < t_root.element:
                t_root = t_root.left
            elif key > t_root.element:
                t_root = t_root.right
        return False

    def inorder(self,t_root):
        if t_root:
            self.inorder(t_root.left)
            print(t_root.element,end=' ')
            self.inorder(t_root.right)

    def Pre_order(self, t_root):
        if t_root:
            print(t_root.element, end=' ')
            self.Pre_order(t_root.left)
            self.Pre_order(t_root.right)


B = BinarySearchTree()
B.insert(B.root, 50)
B.insert(B.root, 30)
B.insert(B.root, 10)
B.inorder(B.root)
print()
B.Pre_order(B.root)
print()
print(B.search(30))
print(B.search(70))
