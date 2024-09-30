from collections import deque

C = int(input())
imp = []

for _ in range(C):
    ip = deque(input().split())

    dq = deque()
    bn = True

    for simb in ip:
        if simb in '{[(':
            dq.append(simb)
        elif simb in ')]}':
            if len(dq) == 0:
                bn = False
            elif simb == ')' and dq[-1] == '(':
                dq.pop()
            elif simb == ']' and dq[-1] == '[':
                dq.pop()
            elif simb == '}' and dq[-1] == '{':
                dq.pop()
            else:
                bn = False

    if bn:
        imp.append("correcta")
    else:
        imp.append("incorrecta")

for res in imp:
    print(res)