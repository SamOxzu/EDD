from bisect import bisect_left

C = int(input())
imp = []
i = 0
while i < C:
    N = list(map(int, input().split()))
    N = sorted(N)
    cont = [0] * len(N)
    for n in N:
        j = bisect_left(N,n)
        cont[j] = cont[j]+1
    res = ""
    for m in cont:
        if m != 0:
            if res == "":
                res = res+str(m)
            else:
                res = res+" "+str(m)
    imp.append(res)
    i = i + 1

for res in imp:
    print(res)
    