import heapq

A = []
B = []
C = []
punt = [0,0,0]

while True:
    ipt = input().split()
    com = ipt[0]

    if com == "A":
        heapq.heappush(A,int(ipt[1]))
    elif com == "B":
        heapq.heappush(B,int(ipt[1]))
    elif com == "C":
        heapq.heappush(C,int(ipt[1]))
    elif com == "menores":

        repA = heapq.heappop(A) if A else 1001
        repB = heapq.heappop(B) if B else 1001
        repC = heapq.heappop(C) if C else 1001

        if repA == 1001 and repB == 1001 and repC == 1001:
            pass
        elif repA == repB and repB == repC:
            punt[0] = punt[0] + 1
            punt[1] = punt[1] + 1
            punt[2] = punt[2] + 1
        elif repA == repB:
            if repA < repC:
                punt[0] = punt[0] + 1
                punt[1] = punt[1] + 1
            else:
                punt[2] = punt[2] + 1
        elif repA == repC:
            if repA < repB:
                punt[0] = punt[0] + 1
                punt[2] = punt[2] + 1
            else:
                punt[1] = punt[1] + 1
        elif repB == repC:
            if repB < repA:
                punt[1] = punt[1] + 1
                punt[2] = punt[2] + 1
            else:
                punt[0] = punt[0] + 1
        elif repA < repB and repA < repC:
            punt[0] = punt[0] + 1
        elif repB < repA and repB < repC:
            punt[1] = punt[1] + 1
        elif repC < repA and repC < repB:
            punt[2] = punt[2] + 1

    elif com == "fin":
        break

print("Equipo A: "+str(punt[0]))
print("Equipo B: "+str(punt[1]))
print("Equipo C: "+str(punt[2]))