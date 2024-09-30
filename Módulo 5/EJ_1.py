nums = list()
imp = []
while True:
    ip = input().split()
    com = ip[0]
    if com == "E":
        break
    elif com == "A":
        nums.append(int(ip[1]))
    elif com == "M":
        suma = 0
        for num in nums:
            if num % int(ip[1]) == 0:
                suma = suma + num
        imp.append(suma)

for res in imp:
    print(res)