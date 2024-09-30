from collections import deque

ip = list(map(int,input().split()))
N = ip[0]
T = ip[1]
revs = deque()

for _ in range(N):
    rev = list(map(int, input().split()))
    revs.append(rev)

i = 1
ult = ""
while T > 0 and revs:
    rev = revs[0]
    if T <= int(rev[1]):
        print(f"{rev[0]} {T}")
        exit()
    else:
        T = T - rev[1]
        if i == 5:
            revs.popleft()
            i = 1
        else:
            revs.append(revs.popleft())
            i = i+1

if not revs:
    if T > 0:
        print("quedaron boletas disponibles")