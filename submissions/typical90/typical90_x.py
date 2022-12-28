N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

differ = []

for i in range(N):
    differ.append(abs(B[i] - A[i]))

differ_sum = sum(differ)

if differ_sum <= K and (K - differ_sum) % 2 == 0:
    print("Yes")
else:
    print("No")
