N = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))

dp = [10**9] * (N + 10)
# root = [0] * (N + 10)

dp[0] = 0
dp[1] = 0
dp[2] = A[2]

# root[0] = -1
# root[1] = [1]
# root[2] = [1, 2]

for i in range(3, N + 1):
    used_A = dp[i - 1] + A[i]
    used_B = dp[i - 2] + B[i]
    if used_A >= used_B:
        dp[i] = used_B
        # root[i] = root[i - 2] + [i]
    else:
        dp[i] = used_A
        # root[i] = root[i - 1] + [i]


# print(dp[N])
# print(dp)
ans_root = [N]
i = N
while i >= 3:
    root_A = dp[i - 1] + A[i]
    root_B = dp[i - 2] + B[i]

    if root_B <= root_A:
        ans_root.append(i - 2)
        i -= 2
    else:
        ans_root.append(i - 1)
        i -= 1
else:
    if i == 2:
        ans_root.append(1)

print(len(ans_root))
print(*reversed(ans_root))

# print(ans_root)

# print(root)
# print(len(root[N]))
# print(*root[N])
