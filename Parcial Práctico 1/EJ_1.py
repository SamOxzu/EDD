from collections import deque

Q = int(input())
cilin = deque()

for _ in range(Q):
    com = list(map(int, input().split()))

    if com[0] == 1:
        for _ in range(com[2]):
            cilin.append(com[1])

    elif com[0] == 2:
        sum = 0
        for _ in range(com[1]):
            sum = sum + cilin.popleft()
        print(sum)