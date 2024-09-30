import heapq

C = int(input())
imp = []

for _ in range(C):
    ipt = list(map(int, input().split()))
    N = ipt[0]
    A = ipt[1]
    B = ipt[2]
    hp = []

    for i in range(N):
        heapq.heappush(hp,i+1)

    while len(hp) > 1:
        hpt = []
        for i in hp:
            heapq.heappush(hpt, (i*A)%B)
        hp = hpt
        
        for _ in range(len(hp)//2):
            heapq.heappop(hp)

    imp.append(hp[0])

for sol in imp:
    print(sol)