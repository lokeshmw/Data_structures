class Node:

    def __init__(self, element, left=None, right=None):
        self.left = left
        self.right = right
        self.element = element


class Binarytree:

    def __init__(self):
        self.root = None

    def build_tree(self, e, left, right):
        self.root = Node(e, left.root, right.root)

    def inorder(self, temp_root):
        if temp_root:
            self.inorder(temp_root.left)
            print(temp_root.element, end=" ")
            self.inorder(temp_root.right)

    def preorder(self, t_root):
        if t_root:
            print(t_root.element, end=" ")
            self.preorder(t_root.left)
            self.preorder(t_root.right)

    def postorder(self, t_root):
        if t_root:
            self.postorder(t_root.left)
            self.postorder(t_root.right)
            print(t_root.element, end=" ")

    def count(self, temp_root):
        if temp_root:
            c = self.count(temp_root.left)
            d = self.count(temp_root.right)
            return c + d + 1
        return 0

    def height(self, temp_root):
        if temp_root:
            s = self.height(temp_root.left)
            r = self.height(temp_root.right)
            if s > r:
                return s + 1
            else:
                return r + 1
        return 0


x = Binarytree()
y = Binarytree()
z = Binarytree()
a_none = Binarytree()
x.build_tree(20, a_none, a_none)
y.build_tree(30, a_none, a_none)
z.build_tree(10, x, y)
print('Inorder Traversal')
z.inorder(z.root)
print()
print('Preorder Traversal')
z.preorder(z.root)
print()
print('Postorder Traversal')
z.postorder(z.root)
print()
print('Number of Nodes: ', z.count(z.root))
print('height: ', z.height(z.root)-1)

