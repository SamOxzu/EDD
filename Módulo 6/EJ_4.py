import heapq

C = int(input())
imp = []

for _ in range(C):
    wtf = int(input())
    nums = input().split()
    hp = []
    for num in nums:
        heapq.heappush(hp, num)

    X = ""
    Y = ""
    while len(hp) > 0:
        X = X+heapq.heappop(hp)
        if hp:
            Y = Y+heapq.heappop(hp)

    msum = int(X) + int(Y)
    imp.append(msum)

for sol in imp:
    print(sol)