C = int(input())
imp = []
for _ in range(C):
    conexiones = {}
    R = int(input())
    for _ in range(R):
        registro = tuple(map(int, input().split()))
    
        if registro[0] not in conexiones:
            conexiones[registro[0]] = {registro[1]}
        else:
            conexiones[registro[0]].add(registro[1])
        
        if registro[1] not in conexiones:
            conexiones[registro[1]] = {registro[0]}
        else:
            conexiones[registro[1]].add(registro[0])
        
    # DFS Para determinar cuántos sub-grafos hay, y qué tamaño tiene el más grande
    visitados = set()
    subgrafos = 0
    tamano_max = 0
    for nodo in conexiones:
        if nodo not in visitados:
            subgrafos += 1
            tamano = 0
            pila = [nodo]
            visitados.add(nodo)
            while pila:
                actual = pila.pop()
                tamano += 1
                for vecino in conexiones[actual]:
                    if vecino not in visitados:
                        visitados.add(vecino)
                        pila.append(vecino)
            if tamano > tamano_max:
                tamano_max = tamano
    imp.append(f"{subgrafos} {tamano_max}")

for res in imp:
    print(res)