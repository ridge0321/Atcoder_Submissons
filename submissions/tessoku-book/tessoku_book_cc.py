N = str(input())
# print(int(N, 2))
n_list = list(N)

ans = 0
for i in range(len(n_list)):
    ans += int(n_list[i]) * (2 ** (len(n_list) - i - 1))

print(ans)
