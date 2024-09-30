from bisect import bisect_left, bisect, bisect_right

N = int(input())
val = list(map(int, input().split()))
M = int(input())
elem = list(map(int, input().split()))
sum = 0
for e in elem:
    i = bisect_left(val, e)

    if i != N and val[i] == e:
        sum = sum + i + 1
print(sum)