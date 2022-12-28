N = int(input())
W = [str(input()) for i in range(N)]

w_dict = {}
ans = "Yes"

for i in range(N - 1):
    if W[i] not in w_dict:
        w_dict[W[i]] = 1
    else:
        ans = "No"
        break

    now_w_list = list(W[i])
    next_w_list = list(W[i + 1])

    now_last = now_w_list[len(now_w_list) - 1]
    next_first = next_w_list[0]

    if not (now_last == next_first):
        ans = "No"
        break
else:
    if W[N - 1] not in w_dict:
        w_dict[W[N - 1]] = 1
    else:
        ans = "No"


print(ans)
