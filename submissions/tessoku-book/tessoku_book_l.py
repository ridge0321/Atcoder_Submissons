import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))


L = 1
R = 10**9
ans = None
while L < R:
    M = (L + R) // 2
    # print(M)

    pages_count = 0

    for a in A:
        pages_count += M // a

    if pages_count >= K:
        R = M
    else:
        L = M + 1
else:
    ans = L

print(ans)
