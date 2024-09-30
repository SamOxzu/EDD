rbt = set()

inc = int(input())
for i in range(inc):
    rbt.add(i+1)

imp = list()

while True:
    cmd = input().split()
    if cmd[0] == 'new':
        son = int(cmd[1]) + int(cmd[2])
        while True:
            if son not in rbt:
                rbt.add(son)
                break
            son += 1
    elif cmd[0] == 'search':
        if int(cmd[1]) in rbt:
            imp.append('existe')
        else:
            imp.append('no existe')
    elif cmd[0] == '#':
        break

for res in imp:
    print(res)