konoha_born = set()
konoha_death = set()
konoha_alive = set()

while True:
    cmd = input().split()
    if cmd[0] == 'E':
        break
    elif cmd[0] == 'B':
        if cmd[1] not in konoha_born:
            konoha_born.add(cmd[1])
            konoha_alive.add(cmd[1])
    elif cmd[0] == 'D':
        if cmd[1] in konoha_alive:
            konoha_alive.remove(cmd[1])
            konoha_death.add(cmd[1])
    elif cmd[0] == 'R':
        if cmd[1] in konoha_death:
            konoha_death.remove(cmd[1])
            konoha_alive.add(cmd[1])

print(len(konoha_alive))