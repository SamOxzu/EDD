import math

N = int(input())
MANGO = list(input().split(", "))
MANGO_ARCOIRIS = []
i = 0
j = 1

while i < math.ceil(N/2):
    MANGO_ARCOIRIS.append(MANGO[i])
    MANGO_ARCOIRIS.append(MANGO[N-j])
    i = i+1
    j = j+1

if N % 2 == 1:
    MANGO_ARCOIRIS.pop()

print("".join(MANGO_ARCOIRIS))
