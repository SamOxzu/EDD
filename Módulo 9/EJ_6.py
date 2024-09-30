guerrillos = set()
tibios = set()
paracos = set()

while True:
    cmd = input().split()
    if cmd[0] == '#':
        break
    part = cmd[1]
    if part == 'pdd':
        paracos.add(cmd[0])
    elif part == 'pdc':
        tibios.add(cmd[0])
    elif part == 'pdi':
        guerrillos.add(cmd[0])

extremistas = len(guerrillos-tibios-paracos) + len(tibios-paracos-guerrillos) + len(paracos-guerrillos-tibios)
moderados = len((guerrillos & tibios) - paracos) + len((tibios & paracos) - guerrillos) + len((paracos & guerrillos) - tibios)
indiferentes = len(guerrillos & tibios & paracos)

print(f"{extremistas} {moderados} {indiferentes}")