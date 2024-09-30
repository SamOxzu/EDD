from bisect import bisect_left, bisect_right

C = int(input())
imp = []

for _ in range(C):
    ip1 = list(map(int, input().split()))
    N = ip1[0]
    P = ip1[1]
    ip2 = list(map(int, input().split()))

    divP = [1]
    for j in range(2, int(P**0.5) + 1):
        if P % j:
            continue
        divP.append(j)
        divP.append(int(P/j))
    divP.append(P)

    es = True
    for k in divP:
        if k not in ip2:
            es = False
            break

    if es:
        imp.append("Es PrimiConjunto")
    else:
        imp.append("No es PrimiConjunto")

for res in imp:
    print(res)