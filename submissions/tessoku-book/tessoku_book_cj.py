import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())

for _ in range(Q):
    X = int(input())
    L = 1
    R = N

    ans = bisect.bisect_left(A, X)

    print(ans)
