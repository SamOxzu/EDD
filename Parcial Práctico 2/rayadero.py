from bisect import *

ip1 = list(map(int, input().split()))
num_eventos = ip1[0]
num_consultas = ip1[1]

ip2 = list(input().split())
eventos = sorted(ip2)

for _ in range(num_consultas):
    ip3 = list(input().split())
    evento = ip3[0]
    veces_pregunta = int(ip3[1])
    veces_reales = abs(bisect_left(eventos,evento)-bisect_right(eventos,evento))
    if (evento not in eventos):
        print('NO')
        continue
    elif (veces_reales >= veces_pregunta):
        print('SI')
    else:
        print('NO')