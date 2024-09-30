class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key)

    def _insertRecursively(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insertRecursively(root.left, key)
        elif key > root.key:
            root.right = self._insertRecursively(root.right, key)
        return root

    def search(self, key):
        if self._searchRecursively(self.root, key) != None:
            return True
        else:
            return False

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        return self._searchRecursively(root.right, key)

    def delete(self, key):
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._minValueNode(root.right).key
            root.right = self._deleteRecursively(root.right, root.key)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inOrder(self):
        elements = []
        self._inOrderRecursively(self.root, elements)
        return elements

    def _inOrderRecursively(self, root, elements):
        if root:
            self._inOrderRecursively(root.left, elements)
            elements.append(root.key)
            self._inOrderRecursively(root.right, elements)

    def preOrder(self):
        elements = []
        self._preOrderRecursively(self.root, elements)
        return elements

    def _preOrderRecursively(self, root, elements):
        if root:
            elements.append(root.key)
            self._preOrderRecursively(root.left, elements)
            self._preOrderRecursively(root.right, elements)

    def height(self):
        return self._heightRecursively(self.root)

    def _heightRecursively(self, root):
        if root is None:
            return 0
        else:
            left_height = self._heightRecursively(root.left)
            right_height = self._heightRecursively(root.right)
            return max(left_height, right_height) + 1
    
    def leafNodes(self):
        self.leafs = 0
        self._leafNodesRecursively(self.root)
        return self.leafs

    def _leafNodesRecursively(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.leafs += 1
        self._leafNodesRecursively(root.left)
        self._leafNodesRecursively(root.right)

    def onlyChild(self):
        self.onlies = 0
        self._onlyChildRecursively(self.root)
        return self.onlies

    def onlyChildRecursively(self, root):
        if not root:
            return
        if not root.left and root.right:
            self.onlies += 1
            self._leafNodesRecursively(root.right)
        if not root.right and root.left:
            self.onlies += 1
            self._leafNodesRecursively(root.left)
        else:
            self._leafNodesRecursively(root.left)
            self._leafNodesRecursively(root.right)

C = int(input())
imp = []

for _ in range(C):
    ipt = list(map(int, input().split()))
    arb = BinarySearchTree()
    for i in ipt:
        if i != -1:
            arb.insert(i)
    imp.append(arb.leafNodes())

for res in imp:
    print(res)
