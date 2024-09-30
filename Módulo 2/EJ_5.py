C = int(input())
i = 0
imp = []
while i < C:
    M = list(map(int, input().split()))
    N = list(map(int, input().split()))
    ganancias = []
    k = 0
    while k < M[0]:
        ganancias.append(0)
        k = k+1

    j = 0
    for B in N:
        ganancias[j] = ganancias[j] + B
        if j == M[0]-1:
            j = 0
        else:
            j = j+1
    
    ganancias.sort()
    imp.append(ganancias[-1]-ganancias[0])

    i = i+1

for res in imp:
    print(res)