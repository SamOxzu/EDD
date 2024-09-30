from collections import deque

uro = deque()

while True:
    ent = input().split()
    orden = ent[0]
    if orden == "agrega":
        uro.append(ent[1])
    elif orden == "engulle":
        if len(uro) > 1:
            if int(uro[0]) > int(uro[-1]):
                uro.pop()
            elif int(uro[0]) <= int(uro[-1]):
                uro.popleft()
        elif len(uro) == 1:
            uro.pop()
    elif orden == "termina":
        break

if len(uro) >= 1:
    print(f"cabeza {uro[0]} cola {uro[-1]}")
else:
    print("uroboro vacio")