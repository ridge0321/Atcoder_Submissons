N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_a = sum(A)
cum_sum_a = []
for i in range(0, N):
    if i == 0:
        cum_sum_a.append(A[i])
    else:
        cum_sum_a.append(cum_sum_a[i - 1] + A[i])


# print(cum_sum_a)

remainder = X % sum_a
quotient = X // sum_a
ans = N * quotient

for i in range(N):
    if cum_sum_a[i] > remainder:
        ans += i + 1
        break

print(ans)
