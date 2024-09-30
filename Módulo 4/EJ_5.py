from collections import deque


C = int(input())
imp = []

for _ in range(C):
    ip1 = list(map(int, input().split()))
    tci = ip1[0]
    pelf = ip1[1]

    ip2 = deque(map(int, input().split()))

    tiempo = 0
    penelf = ip2[pelf-1]

    while penelf > 0:
        ip2[0] = ip2[0]-1
        tiempo = tiempo+5
        penelf = ip2[pelf-1]
            
        if penelf == 0:
            break

        if ip2[0] == 0:
            ip2.popleft()
        else:
            ip2.append(ip2.popleft())

        if pelf > 1:
            pelf = pelf-1
        else:
            pelf = len(ip2)

    imp.append(tiempo)

for res in imp:
    print(res)