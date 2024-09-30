import heapq

turn = []

while True:
    ipt = input()

    if ipt == "end":
        break
    elif ipt == "sig":
        if turn:
            last = heapq.heappop(turn)
    else:
        heapq.heappush(turn, int(ipt))

if last:
    print(last)