N, Q = map(int, input().split())
A = list(map(int, input().split()))

cum_sum_A = [0]
for i in range(0, len(A)):
    cum_sum_A.append(cum_sum_A[i] + A[i])


for _ in range(Q):
    L, R = map(int, input().split())
    ans = cum_sum_A[R] - cum_sum_A[L - 1]
    print(ans)
