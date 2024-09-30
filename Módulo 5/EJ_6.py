fila = list()

while True:
    fan = input()
    if fan == "0 0":
        break
    fan = list(fan.split())
    if int(fan[1]) <= len(fila):
        continue
    else:
        fila.append(fan)
    
    i = 0
    while i < len(fila):
        if int(fila[len(fila)-i-1][1]) < len(fila):
            fila.remove(fila[len(fila)-i-1])
            break
        i = i+1

print(len(fila))