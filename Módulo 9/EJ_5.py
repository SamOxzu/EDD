fer = set()
gus = set()

while True:
    cmd = input().split()
    if cmd[0] == '0':
        break
    isbn = int(cmd[0])
    if cmd[1] == 'G':
        if isbn not in fer:
            gus.add(isbn)
        elif isbn%2 != 0:
            fer.remove(isbn)
            gus.add(isbn)

    elif cmd[1] == 'F':
        if isbn not in gus:
            fer.add(isbn)
        elif isbn%2 == 0:
            gus.remove(isbn)
            fer.add(isbn)

print(len(fer), len(gus))