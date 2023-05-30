import bisect

N = int(input())
A = list(map(int, input().split()))

A_sorted = [0] + sorted(list(set(A)))
ans = []

for a in A:
    ans.append(bisect.bisect_left(A_sorted, a))

print(*ans)
