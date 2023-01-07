N = int(input())

num_list = [True] * (2 * N + 2)

for i in range(len(num_list)):
    for j in range(1, len(num_list)):
        if num_list[j]:
            print(j)
            num_list[j] = False
            break

    aoki_num = int(input())
    num_list[aoki_num] = False
