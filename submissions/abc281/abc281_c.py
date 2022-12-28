N, T = map(int, input().split())
A = list(map(int, input().split()))

a_sum = sum(A)
t_over = T % a_sum
cum_a_sum = [A[0]]

for i in range(1, len(A)):
    cum_a_sum.append(cum_a_sum[i - 1] + A[i])

for i in range(len(cum_a_sum)):
    if cum_a_sum[i] >= t_over:
        if i == 0:
            ans_s = t_over
        else:
            ans_s = t_over - cum_a_sum[i - 1]
        print("%d %d" % (i + 1, ans_s))
        quit()
