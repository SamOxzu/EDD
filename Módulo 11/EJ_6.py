from collections import deque

def ajedrez_a_matriz(pos):
    col = ord(pos[0]) - ord('A')
    row = int(pos[1]) - 1
    return (row, col)

def es_valido(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def min_movimientos_caballo(inicio, fin):
    if inicio == fin:
        return 0
    
    movimientos = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    cola = deque([(inicio[0], inicio[1], 0)])
    visitado = set()
    visitado.add(inicio)
    
    while cola:
        x, y, dist = cola.popleft()
        
        for mov in movimientos:
            nx, ny = x + mov[0], y + mov[1]
            
            if (nx, ny) == fin:
                return dist + 1
            
            if es_valido(nx, ny) and (nx, ny) not in visitado:
                visitado.add((nx, ny))
                cola.append((nx, ny, dist + 1))
    
    return -1

C = int(input())

for _ in range(C):
    pos_inicio, pos_fin = input().split()
    inicio = ajedrez_a_matriz(pos_inicio)
    fin = ajedrez_a_matriz(pos_fin)
    print(min_movimientos_caballo(inicio, fin))