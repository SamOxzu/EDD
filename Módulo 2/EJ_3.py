C = int(input())
i = 0
msgs = []

while i < C:
    msgs.append(list(input().split()))
    i = i + 1

for msg in msgs:
    msg = msg[::-1]
    j = 0
    while j < len(msg) - 1:
        if j % 2 == 0:
            msg[j], msg[j + 1] = msg[j + 1], msg[j]
        j = j + 1
    print("".join(msg))