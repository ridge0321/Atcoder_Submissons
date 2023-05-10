N = int(input())
A = list(map(int, input().split()))
D = int(input())

max_log_L = [0] * N
max_log_R = [0] * N

max_log_L[0] = A[0]
max_log_R[N - 1] = A[N - 1]

for i in range(1, N):
    if A[i] > max_log_L[i - 1]:
        max_log_L[i] = A[i]
    else:
        max_log_L[i] = max_log_L[i - 1]

for i in reversed(range(0, N - 1)):
    if A[i] > max_log_R[i + 1]:
        max_log_R[i] = A[i]
    else:
        max_log_R[i] = max_log_R[i + 1]


for _ in range(D):
    L, R = map(int, input().split())
    ans = max(max_log_L[L - 2], max_log_R[R])
    print(ans)
