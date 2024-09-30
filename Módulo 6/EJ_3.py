import heapq

C = int(input())
imp = []

for _ in range(C):
    hp = []
    ipt = list(map(int, input().split()))
    for itm in ipt:
        if itm != -1:
            heapq.heappush(hp,itm)
    while len(hp) > 2:
        acm = heapq.heappop(hp) + heapq.heappop(hp)
        heapq.heappush(hp,acm)
    imp.append(f"{hp[0]} {hp[1]}")

for sol in imp:
    print(sol)