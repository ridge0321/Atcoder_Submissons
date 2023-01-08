N = int(input())
A = list(map(int, input().split()))

count_dict = {}

for a in A:
    if a not in count_dict:
        count_dict[a] = 1
    else:
        count_dict[a] += 1

# print(count_dict)

ans = 0
i = 0
for key in A:
    # print(count_dict[key])
    ans += N - i - count_dict[key]

print(ans // 2)
