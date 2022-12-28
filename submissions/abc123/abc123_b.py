ABCDE = [int(input()) for i in range(5)]

loss_time_list = []

for t in ABCDE:
    t_str_list = list(str(t))
    loss_time = 10 - int(t_str_list[len(t_str_list) - 1])

    if loss_time == 10:
        loss_time = 0

    loss_time_list.append(loss_time)

# print(loss_time_list)
# print(loss_time_list.index(max(loss_time_list)))

min_time = sum(ABCDE) + sum(loss_time_list) - max(loss_time_list)
print(min_time)
