M = int(input())
serie = list()
imp = []

while True:
    new = int(input())
    if new == 0:
        break
    serie.append(new)

    serie.sort()

    if len(serie) % M == 0:
        mitad = len(serie) // 2
        if len(serie) % 2 == 0:
            if (serie[mitad]+serie[mitad-1]) % 2 == 0:
                imp.append(int((serie[mitad]+serie[mitad-1])/2))
            else:
                imp.append(f"{serie[mitad]+serie[mitad-1]}/2")            
        else:
            imp.append(serie[mitad])

for res in imp:
    print(res)