from collections import deque

C = int(input())
imp = []

for _ in range(C):
    discs = int(input())
    moves = deque()

    while not moves or moves[-1] != "X X":
        moves.append(input())
    
    moves.pop()

    A = deque()
    B = deque()
    C = deque()
    
    i = discs

    while 0 < i:
        A.append(i)
        i = i-1

    R = A.copy()
    error = False

    for move in moves:
        ipt = move.split()
        P = ipt[0]
        Q = ipt[1]

        if P == Q:
            continue
        if P == "A":
            P = A
        elif P == "B":
            P = B
        elif P == "C":
            P = C
        if Q == "A":
            Q = A
        elif Q == "B":
            Q = B
        elif Q == "C":
            Q = C
        
        if not P:
            error = True
            break

        if Q and P[-1] > Q[-1]:
            error = True
            break
        else:
            Q.append(P.pop())
    
    if error:
        imp.append("secuencia invalida")
    elif C == R:
        imp.append("soluciona la torre")
    else:
        imp.append("no soluciona la torre")

for res in imp:
    print(res)