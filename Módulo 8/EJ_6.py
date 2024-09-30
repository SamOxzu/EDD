from collections import deque
import sys
input = sys.stdin.read

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
 
class AVLTree:
    def __init__(self):
        self.root = None
 
    def insert(self, root, key):
        # Inserción estándar de AVL
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
     
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
 
   
        balance = self.get_balance(root)
 
      
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
 
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
 
 
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
 
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
 
        return root
 
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
 
        return y
 
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
 
        return y
 
    def get_height(self, node):
        if not node:
            return 0
        return node.height
 
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
 
    def subarbol(self, nodo):
  
        def calcular_altura(nodo_actual):
            if nodo_actual is None:
                return 0, True, 0 
 
            altura_izquierda, completo_izquierda, maximo_izquierda = calcular_altura(nodo_actual.left)
            altura_derecha, completo_derecha, maximo_derecha = calcular_altura(nodo_actual.right)
 
            altura_total = 1 + max(altura_izquierda, altura_derecha)
 
            if completo_izquierda and completo_derecha and altura_izquierda == altura_derecha:
              
                es_completo = True
                maximo_completo = altura_total
            else:
               
                es_completo = False
                maximo_completo = max(maximo_izquierda, maximo_derecha)
 
            return altura_total, es_completo, maximo_completo
 
        _, _, maximo_parcial = calcular_altura(nodo)
        return maximo_parcial
 
 
data = input().split()
indice = 0
while indice < len(data):
    cantidad = int(data[indice])
    indice +=1
    if cantidad ==0:
        break
    valores = []
    for _ in range(cantidad):
        if indice < len(data):
            valores.append(int(data[indice]))
            indice +=1
    arbol = AVLTree()
    raiz = None
    for valor in valores:
        raiz = arbol.insert(raiz, valor)
    print(arbol.subarbol(raiz))