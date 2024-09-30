ewok_dict = dict()

N = int(input())

for _ in range(N):
    mean = input().split()
    ewok_dict[mean[0]] = mean[1]

while True:
    cmd = input()
    if cmd == '#':
        break
    if cmd in ewok_dict:
        mean = ewok_dict[cmd]
        print(mean)
    else:
        print("Entrada no encontrada")