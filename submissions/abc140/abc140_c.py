N = int(input())
B = list(map(int, input().split()))

A = [B[0], B[0]]

for i in range(1, N - 1):
    if A[i] > B[i]:
        A[i] = B[i]
    A.append(B[i])

print(sum(A))
