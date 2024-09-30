C = int(input())
imp = []

for _ in range(C):
    ip = list(map(int, input().split()))
    N = ip[0]
    K = ip[1]

    est = list(range(1, N+1))

    posicion = 0
    while len(est) > 1:
        posicion = (posicion + K - 1) % len(est)
        K = est[posicion] % (len(est)-1)
        if K == 0:
            K = 1
        est.pop(posicion)

    imp.append(est[0])

for res in imp:
    print(res)