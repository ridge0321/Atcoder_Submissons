N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]
count_dict = {}
for i in range(1, N + 1):
    count_dict[i] = 0

for a in A:
    count_dict[a] += 1

# print(count_dict)

for i in range(1, N + 1):
    correct_point = count_dict[i]
    remain_point = K - Q + correct_point
    if remain_point > 0:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)