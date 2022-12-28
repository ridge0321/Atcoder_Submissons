N, Q = map(int, input().split())
A = list(map(int, input().split()))
differ_A = []
dif_abs_A = []


for i in range(1, len(A)):
    differ_A.append(A[i] - A[i - 1])
    dif_abs_A.append(abs(A[i] - A[i - 1]))
abs_sum = sum(dif_abs_A)
ans = []

for i in range(Q):
    L, R, V = map(int, input().split())
    before_l = 0
    before_r = 0
    after_l = 0
    after_r = 0

    if not (L == 1):
        l_index = L - 2
        before_l = abs(differ_A[l_index])

        differ_A[l_index] = differ_A[l_index] + V
        after_l = abs(differ_A[l_index])

        # temp_l_abs = dif_abs_A[l_index]

        # dif_abs_A[l_index] = abs(differ_A[l_index])

    if not (R == N):
        r_index = R - 1
        before_r = abs(differ_A[r_index])
        differ_A[r_index] = differ_A[r_index] - V
        after_r = abs(differ_A[r_index])

        # temp_r_abs = dif_abs_A[r_index]
        # dif_abs_A[r_index] = abs(differ_A[r_index])

    abs_sum += (after_l - before_l) + (after_r - before_r)
    ans.append(abs_sum)

for a in ans:
    print(a)
