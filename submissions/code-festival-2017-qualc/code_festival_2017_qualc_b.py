N = int(input())
A = list(map(int, input().split()))

odd_count = 0
for i in range(N):
    if A[i] % 2 == 0:
        odd_count += 1


print(3 ** len(A) - 2**odd_count)