from collections import deque

C = int(input())
imp = []

for _ in range(C):
    piezas = deque((map(int, input().split())))
    while len(piezas) >= 2:
        if (piezas[-1] + piezas[-2]) % 2 == 0:
            new = int((piezas[-1]+piezas[-2]) / 2)
            piezas.pop()
            piezas.pop()
            piezas.append(new)
        else:
            break

    imp.append(f"{len(piezas)} {piezas[-1]}")

for res in imp:
    print(res)