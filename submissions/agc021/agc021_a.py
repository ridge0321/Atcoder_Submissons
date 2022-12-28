N = list(str(input()))

n_int_list = list(map(int, N))
ans_list = []

for i in range(len(n_int_list)):
    if i == 0:
        ans_list.append(n_int_list[0] - 1)
    else:
        ans_list.append(9)

ans_list_sum = sum(ans_list)
default_sum = sum(n_int_list)

print(max(ans_list_sum, default_sum))
