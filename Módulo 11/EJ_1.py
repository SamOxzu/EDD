C = int(input())
for i in range(C):
    ip1 = tuple(map(int, input().split(', ')))
    I = ip1[0]
    B = ip1[1]
    invitados = [[] for _ in range(I)]
    for _ in range(B):
        ip2 = tuple(map(int, input().split()))
        invitados[ip2[0]].append(ip2[1])
        invitados[ip2[1]].append(ip2[0])

    # BFS para determinar a cuantos saltos está un invitado de Paulina (posición 0)
    visitados = [False] * I
    distancias = [0] * I
    cola = [0]
    visitados[0] = True
    while cola:
        actual = cola.pop(0)
        for vecino in invitados[actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                distancias[vecino] = distancias[actual] + 1
                cola.append(vecino)

    print(f"fiesta {i + 1}:")
    for j in range(1, I):
        print(j, distancias[j] if distancias[j] else "INF")
    print() if i != C-1 else None