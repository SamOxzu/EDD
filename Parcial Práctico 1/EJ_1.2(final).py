from collections import deque

cilin = deque()

for _ in range(int(input())):
    com = tuple(map(int, input().split()))

    if com[0] == 1:
        cilin.append([com[1], com[2]])

    elif com[0] == 2:
        req = com[1]
        suma = 0
        while req > 0:
            if req < cilin[0][1]:
                suma = suma + (cilin[0][0]*req)
                cilin[0][1] = cilin[0][1] - req
                break
            else:
                suma = suma + (cilin[0][0] * cilin[0][1])
                req = req - cilin[0][1]
                cilin.popleft()
        print(suma)