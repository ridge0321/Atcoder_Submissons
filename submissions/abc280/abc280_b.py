N = int(input())
A = list(map(int, input().split()))
ans = [A[0]]

for i in range(1, N):
    ans.append(A[i] - A[i - 1])

# print(ans)
# print(" ".join(ans))

for i in range(len(ans)):
    if i == len(ans) - 1:
        print("%d" % (ans[i]))
    else:
        print("%d " % (ans[i]), end="")
