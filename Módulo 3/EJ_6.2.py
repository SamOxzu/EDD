C = int(input())
imp = []

for _ in range(C):
    a = 0
    pes = sorted(list(map(int, input().split(", "))))
    diferencia = 10000000000
    total = sum(pes)
    for j in range(len(pes)-1):
        a += pes[j]
        diferencia = min(diferencia, total-2*a)
    imp.append(diferencia)

for res in imp:
    print(abs(res))