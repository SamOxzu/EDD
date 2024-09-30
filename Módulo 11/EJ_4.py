C = int(input())
imp = []
for _ in range(C):
    ip1 = tuple(map(int, input().split()))
    N = ip1[0]
    M = ip1[1]
    nodos = [[] for _ in range(N)]
    for _ in range(M):
        ip2 = tuple(map(int, input().split(', ')))
        nodos[ip2[0]-1].append(ip2[1]-1)
        nodos[ip2[1]-1].append(ip2[0]-1)

    # BFS para determinar si el grafo es bipartito
    visitados = [False] * N
    color = [-1] * N
    es_bipartito = True

    def bfs(start):
        cola = [start]
        visitados[start] = True
        color[start] = 0
        while cola:
            actual = cola.pop(0)
            for vecino in nodos[actual]:
                if not visitados[vecino]:
                    visitados[vecino] = True
                    color[vecino] = 1 - color[actual]
                    cola.append(vecino)
                elif color[vecino] == color[actual]:
                    return False
        return True

    for i in range(N):
        if not visitados[i]:
            if not bfs(i):
                es_bipartito = False
                break

    imp.append("bipartito" if es_bipartito else "no bipartito")

for res in imp:
    print(res)