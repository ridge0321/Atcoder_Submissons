import bisect

d = int(input())
n = int(input())
m = int(input())

di = [0]
for _ in range(n - 1):
    di.append(int(input()))

# di = [int(input()) for i in range(n - 1)]
# k = [int(input()) for i in range(m)]

# di.append(0)
di = sorted(di)

result = 0

for temp in range(m):
    k = int(input())

    insertion_p = bisect.bisect_left(di, k)
    if insertion_p == n:
        distance = min(abs(k - di[n - 1]), abs(k - d))
    else:
        distance = min(abs(k - di[insertion_p]), abs(k - di[insertion_p - 1]))

    result += distance

print(result)
