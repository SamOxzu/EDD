C = int(input())
i = 0
imp = []

while i < C:
    Docs = list(map(int, input().split()))
    k = 0
    cont = 0
    while k < len(Docs)-1:
        j = 0
        while j < len(Docs)-1:
            if Docs[j] > Docs[j+1]:
                cont = cont+1
                Docs[j], Docs[j+1] = Docs[j+1], Docs[j]
            j = j+1
        k = k+1
    imp.append(cont)
    i = i+1

for res in imp:
    print(res)