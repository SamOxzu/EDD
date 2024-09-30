dicciojerga = dict()
while True:
    ipt = input()
    if ipt == "#":
        break
    dicciojerga[ipt] = True

palabras_compuestas = []

for palabra in dicciojerga:
    for i in range(1, len(palabra)):
        primera_parte = palabra[:i]
        segunda_parte = palabra[i:]
        if primera_parte in dicciojerga and segunda_parte in dicciojerga:
            palabras_compuestas.append(f"{palabra} = {primera_parte} + {segunda_parte}")

for compuesta in palabras_compuestas:
    print(compuesta)