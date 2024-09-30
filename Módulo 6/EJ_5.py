import heapq

dur = int(input())
ult = 0
sdp = []

nton = int(input())

for _ in range(nton):
    ton = list(map(int, input().split()))
    heapq.heappush(sdp, (ton[1], ton))

while ult <= dur:
    note = heapq.heappop(sdp)
    ult = note[0]
    if ult > dur:
        break
    print(ult)
    newnote = []
    newnote.append(note[1][0])
    newnote.append(note[1][1]+note[1][2])
    newnote.append(note[1][2])
    heapq.heappush(sdp, (newnote[1], newnote))