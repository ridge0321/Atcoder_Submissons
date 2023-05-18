N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))

L = 1
R = N


while L <= R:
    M = (L + R) // 2
    if A[M] == X:
        ans = M
        break
    elif A[M] < X:
        L = M + 1
    elif X < A[M]:
        R = M - 1

print(ans)
