N = int(input())
ent = input().split()
i = 3
suma = 0
suma = suma + int(ent[N-1])+int(ent[N-2])
print(suma)

while i <= N:
    suma = suma + int(ent[N-i])
    print(suma)
    i = i + 1