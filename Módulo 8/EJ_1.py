class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, key):
        if not self.search(key):
            self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        if not root:
            new_node = Node(key)
            self.size += 1
            return new_node
        elif key < root.key:
            root.left = self._insertRecursively(root.left, key)
        else:
            root.right = self._insertRecursively(root.right, key)

        root.height = 1 + max(self._getNodeHeight(root.left),
                              self._getNodeHeight(root.right))

        balanceFactor = self._getNodeBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)

        return root

    def delete(self, key):
        self.size -= self.search(key)
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):

        if not root:
            return root
        elif key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._getMin(root.right)
            root.key = temp
            root.right = self._deleteRecursively(root.right, temp)
        if root is None:
            return root

        root.height = 1 + max(self._getNodeHeight(root.left), self._getNodeHeight(root.right))
        balanceFactor = self._getNodeBalance(root)

        if balanceFactor > 1:
            if self._getNodeBalance(root.left) >= 0:
                return self._rightRotate(root)
            else:
                root.left = self._leftRotate(root.left)
                return self._rightRotate(root)
        if balanceFactor < -1:
            if self._getNodeBalance(root.right) <= 0:
                return self._leftRotate(root)
            else:
                root.right = self._rightRotate(root.right)
                return self._leftRotate(root)
        return root

    def _leftRotate(self, z):
        y = z.right
        aux = y.left
        y.left = z
        z.right = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _rightRotate(self, z):
        y = z.left
        aux = y.right
        y.right = z
        z.left = aux
        z.height = 1 + max(self._getNodeHeight(z.left), self._getNodeHeight(z.right))
        y.height = 1 + max(self._getNodeHeight(y.left), self._getNodeHeight(y.right))
        return y

    def _getNodeHeight(self, root):
        if not root:
            return 0
        return root.height

    def _getNodeBalance(self, root):
        if not root:
            return 0
        return self._getNodeHeight(root.left) - self._getNodeHeight(root.right)

    def _getMin(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root.key
        return self._getMin(root.left)

    def search(self, key):
        return self._searchRecursively(self.root, key) != None

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        else:
            return self._searchRecursively(root.right, key)

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            elements.append(root.key)
            self._inOrderRecursively(root.right, elements)

    def posOrder(self):
        elements = []
        self._posOrderRecursively(self.root, elements)
        return elements

    def _posOrderRecursively(self, root, elements):
        if root:
            self._posOrderRecursively(root.left, elements)
            self._posOrderRecursively(root.right, elements)
            elements.append(root.key)

    def popMin(self):
        if self.size == 0:
            return None
        else:
            key = self._getMin(self.root)
            self.delete(key)
            return key

"""
# Ejemplo de aplicacion
avl = AVLTree()
elms = [13, 74, 48, 21, 99, 35, 60, 82, 57]
for e in elms:
    avl.insert(e)

print(avl.search(35))   # True
print(avl.search(19))   # False

print(avl.inOrder())    # [13, 21, 35, 48, 57, 60, 74, 82, 99]

avl.delete(48)
print(avl.inOrder())    # [13, 21, 35, 57, 60, 74, 82, 99]

print(avl.popMin())     # 13
"""

C = int(input())

for _ in range(C):
    ip = list(input().split())
    avl = AVLTree()
    for itm in ip:
        if itm != "#":
            avl.insert(itm)
    imp = avl.posOrder()
    res = ""
    for itm in imp:
        res += str(itm)
    print(res)