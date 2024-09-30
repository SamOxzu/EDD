P = int(input())
personas = [[] for _ in range(P)]
for i in range(P):
    ip = list(map(int, input().split()))
    if ip[0] == -1:
        continue
    for amigo in ip:
        personas[i].append(amigo)

imp = []
ip2 = tuple(map(int, input().split(', ')))
for T in ip2:
    if personas[T] == []:
        imp.append("0")
        continue
    # BFS
    visitados = [False] * P
    distancias = [0] * P
    cola = [T]
    visitados[T] = True
    max_enterados = 0
    dia_max_enterados = 0
    dia = 0
    while cola:
        dia += 1
        cont_enterados_hoy = 0
        for _ in range(len(cola)):
            actual = cola.pop(0)
            for vecino in personas[actual]:
                if not visitados[vecino]:
                    cont_enterados_hoy += 1
                    visitados[vecino] = True
                    distancias[vecino] = distancias[actual] + 1
                    cola.append(vecino)
        if cont_enterados_hoy > max_enterados:
            max_enterados = cont_enterados_hoy
            dia_max_enterados = dia
    if max_enterados == 0:
        imp.append("0")
    else:
        imp.append(f"{dia_max_enterados} {max_enterados}")

for res in imp:
    print(res)