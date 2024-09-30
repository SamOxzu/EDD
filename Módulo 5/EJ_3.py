fun = True
nums = list()
imp = []

while fun:
    ip = list(input().split())
    com = ip[0]
    if com == "end":
        break
    elif com == "C":
        if nums:
            nums.pop()
    elif com == "D":
        if int(ip[1]) > len(nums):
            pass
        else:
            if nums:
                for _ in range(int(ip[1])):
                    nums.pop()
    elif com == "M":
        i = int(ip[1])
        j = int(ip[2])
        if j > len(nums):
            pass
        else:
            M = ""
            while i <= j:
                M = M+nums[i-1]
                i = i+1
            imp.append(M)
    else:
        nums.append(com)

for res in imp:
    print(res)