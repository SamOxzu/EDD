N = int(input())
i = 0
pos = 0
neg = 0

while i < N:
    N2 = int(input())
    if N2 < 0:
        neg = neg+N2
    else:
        pos = pos+N2
    i = i+1

print(f"positivos {pos}, negativos {neg}")
