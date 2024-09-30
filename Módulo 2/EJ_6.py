C = int(input())
size = []
csl = []
imp = []

for _ in range(C):
    S = int(input())
    size.append(S)
    csl.append(list(map(int, input().split())))

for l, S in enumerate(size):
    A1 = True
    j = 0
    k = 0
    rep = []

    while A1:
        x = rep.count(j)
        if x != 0:
            A1 = False
            imp.append(k)
            k = 0
            j = 0
        elif 0 <= j + csl[l][j] < S:
            rep.append(j)
            j = j + csl[l][j]
            k = k+1
        else:
            A1 = False
            imp.append(k+1)
            k = 0
            j = 0

    A1 = True
    j = 0
    k = 0
    rep = []

for i in imp:
    print(i)