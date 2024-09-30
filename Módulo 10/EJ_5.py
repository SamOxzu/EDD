votantes = dict()
votos = dict()

while True:
    ipt = input().split()
    if ipt[0] == '0' and ipt[1] == '0':
        break
    
    if ipt[0] in votantes:
        votantes[ipt[0]].append(ipt[1])
    else:
        votantes[ipt[0]] = [ipt[1]]

for votante in votantes:
    if len(votantes[votante]) > 1:
        continue
    candidato = int(votantes[votante][0])
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1

# Ordenar los votos en orden descendente y por documento de candidato en orden descendente en caso de empate
votos_ordenados = sorted(votos.items(), key=lambda x: (-x[1], -x[0]))

for candidato, votos in votos_ordenados:
    print(f"{candidato} {votos}")