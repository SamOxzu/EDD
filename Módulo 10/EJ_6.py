def cribaEratostenes(num):
    es_primo = [True] * (num + 1)
    p = 2
    while (p * p <= num):
        if es_primo[p]:
            for i in range(p * p, num + 1, p):
                es_primo[i] = False
        p += 1
    primos = [p for p in range(2, num) if es_primo[p]]
    return primos

N = int(input())
imp = []

for _ in range(N):
    num = int(input())
    primos_menores = cribaEratostenes(num)
    primos_set = set(primos_menores)
    cont = 0
    for primo in primos_menores:
        if (num - primo) in primos_set:
            cont += 1
        if primo * 2 == num:
            cont += 1
    cont //= 2
    imp.append(cont)

for res in imp:
    print(res)