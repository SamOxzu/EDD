def dfs(matrix, x, y, visited):
    stack = [(x, y)]
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha
    
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        count += 1
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and (nx, ny) not in visited and matrix[nx][ny] == 'X':
                stack.append((nx, ny))
    
    return count

C = int(input())
imp = []
for _ in range(C):
    ip1 = tuple(map(int, input().split()))
    A = ip1[0]
    B = ip1[1]
    rectangulo = []
    for _ in range(A):
        rectangulo.append(list(input().strip()))
    
    max_xs = 0
    visited = set()
    
    for i in range(A):
        for j in range(B):
            if rectangulo[i][j] == 'X' and (i, j) not in visited:
                max_xs = max(max_xs, dfs(rectangulo, i, j, visited))
    
    imp.append(max_xs)

for res in imp:
    print(res)