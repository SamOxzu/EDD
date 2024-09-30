C = int(input())
imp = []

for _ in range(C):
    pes = sorted(list(map(int, input().split(", "))))
    mid = len(pes)//2
    izq = pes[:mid]
    der = pes[mid:]
    dif = abs(sum(izq) - sum(der))
    c = True
    while c == True:
        izqt = izq.copy()
        dert = der.copy()
        izqt.append(dert.pop(0))
        dift = abs(sum(izqt) - sum(dert))
        if dift < dif:
            izq = izqt
            der = dert
            dif = dift
        else:
            c = False
    imp.append(dif)

for res in imp:
    print(res)
    



for res in imp:
    print(res)