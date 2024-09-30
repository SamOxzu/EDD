ipt = list(map(int, input().split()))
N = ipt[0]
T = ipt[1]
elements = []

for _ in range(N):
    num = int(input())
    elements.append(num)

# Ordenar la lista de elementos
elements.sort()

ternas = set()

# Usar un bucle para fijar el primer elemento de la terna
for i in range(N - 2):
    # Evitar duplicados para el primer elemento
    if i > 0 and elements[i] == elements[i - 1]:
        continue
    # Usar dos punteros para encontrar los otros dos elementos
    left = i + 1
    right = N - 1
    while left < right:
        suma = elements[i] + elements[left] + elements[right]
        if suma == T:
            # Añadir la terna ordenada al conjunto para evitar duplicados
            terna = (elements[i], elements[left], elements[right])
            ternas.add(terna)
            left += 1
            right -= 1
            # Evitar duplicados para el segundo y tercer elemento
            while left < right and elements[left] == elements[left - 1]:
                left += 1
            while left < right and elements[right] == elements[right + 1]:
                right -= 1
        elif suma < T:
            left += 1
        else:
            right -= 1

if ternas:
    # Ordenar las ternas encontradas
    ternas = sorted(ternas)

    # Imprimir las ternas encontradas
    for terna in ternas:
        print(f"{terna[0]} {terna[1]} {terna[2]}")
else:
    print("No hay trillizas")