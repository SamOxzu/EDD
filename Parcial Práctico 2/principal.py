# womp womp

ip1 = list(map(int, input().split()))
num_eventos = ip1[0]
num_consultas = ip1[1]

ip2 = list(input().split())
eventos = dict()

for evento in ip2:
    if evento in eventos:
        eventos[evento] += 1
    else:
        eventos[evento] = 1

for _ in range(num_consultas):
    ip3 = list(input().split())
    evento = ip3[0]
    veces = int(ip3[1])
    if (evento not in eventos):
        print('NO')
        continue
    elif (eventos[evento] >= veces):
        print('SI')
    else:
        print('NO')