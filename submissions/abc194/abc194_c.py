import itertools

N = int(input())
A = list(map(int, input().split()))


cum_sum = list(itertools.accumulate(A))
mult_sum = 0

# print(cum_sum)

for a in A:
    mult_sum += a**2

mult_sum *= N - 1

interim = 0

for i in range(1, N):
    temp01 = cum_sum[N - 1]
    temp02 = cum_sum[i]
    interim += A[i - 1] * (cum_sum[N - 1] - cum_sum[i - 1])
else:
    interim *= -2

result = mult_sum + interim

print(result)
