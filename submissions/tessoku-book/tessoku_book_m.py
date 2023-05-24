N, K = map(int, input().split())
A = list(map(int, input().split()))
result = 0

R = 1
for i in range(N):
    L = i
    if R <= L:
        R = L + 1

    while R < N:
        if A[R] - A[L] > K:
            result += R - L - 1
            break
        else:
            R += 1
    else:
        result += R - L - 1


print(result)
