from bisect import bisect_left
K = int(input())
CodP = sorted(list(map(int, input().split())))
P = int(input())
i = 0
imp = []
while i < P:
    PosB = sorted(list(map(int, input().split())))
    dif = int(bisect_left(CodP, PosB[1])) - int(bisect_left(CodP,PosB[0]))
    imp.append(dif)
    i = i+1

for res in imp:
    print(f"{res} kms")