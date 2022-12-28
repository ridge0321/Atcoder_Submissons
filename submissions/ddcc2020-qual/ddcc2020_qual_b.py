N = int(input())
A = list(map(int, input().split()))
a_len = sum(A)

cum_sum = [A[0]]
result = []

for i in range(1, N):
    cum_sum.append(cum_sum[i - 1] + A[i])

# print(cum_sum)

for i in range(len(cum_sum)):
    right_len = a_len - cum_sum[i]

    result.append(abs(right_len - cum_sum[i]))

print(min(result))
