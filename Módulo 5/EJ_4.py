jug = list()
while True:
    np = int(input())
    kill = list()
    if np == 0:
        break
    if np in jug:
        kill.append(np)
    elif np+1 in jug:
        kill.append(np+1)
    elif np-1 in jug:
        kill.append(np-1)
    if not kill:
        jug.append(np)

    for lsr in kill:
        jug.remove(lsr)

win = " ".join(str(py) for py in jug)

if win:
    print(win)
else:
    print(0)