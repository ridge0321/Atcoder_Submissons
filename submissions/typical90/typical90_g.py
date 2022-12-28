import bisect

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())
B = [int(input()) for i in range(Q)]


for b in B:
    insert_point = bisect.bisect_left(A, b)
    if insert_point == 0:
        ans = abs(b - A[insert_point])
    elif insert_point == N:
        ans = abs(b - A[N - 1])
    else:
        ans = min(abs(b - A[insert_point]), abs(b - A[insert_point - 1]))

    print(ans)
