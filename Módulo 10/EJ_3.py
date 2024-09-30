from collections import deque


M = int(input())
lottery = set()
winners = deque()
guesses = {}

while True:
    ipt = tuple(input().split())

    if ipt[0] == "end":
        break

    elif ipt[0] == "winner":
        lottery.add(ipt[1])
    
    elif ipt[0] == "sms":
        # Aumentar o inicializar contador de chances con el número
        if ipt[1] in guesses:
            guesses[ipt[1]] += 1
        else:
            guesses[ipt[1]] = 1
        
        # Verificar si el número es ganador
        if ipt[1] in lottery:
            money = int(M/(len(lottery)*guesses[ipt[1]]))
            
            # Agregar el ganador al deque winners
            winners.append((ipt[1], money))

if winners:
    for winner in winners:
        print(f"{winner[0]} {winner[1]}")
else:
    print(0)