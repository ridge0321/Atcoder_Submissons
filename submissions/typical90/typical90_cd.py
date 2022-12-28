L, R = map(str, input().split())

mod = 10**9 + 7


def zero_to_n_count(str_num):
    str_length = len(str_num)
    int_num = int(str_num)
    result = []
    prev = 0
    if str_length == 1:
        result.append((int_num + 1) / 2 * int_num)
    else:
        for i in range(1, str_length):
            if i == 1:
                result.append(45)
                prev = 45
            else:
                # 各桁の数の総和
                temp_sum = (10**i) * (10**i - 1) // 2 - prev

                result.append(temp_sum * i % mod)
                prev = (10**i) * (10**i - 1) // 2

        else:
            temp_sum = int_num * (int_num + 1) // 2 - prev
            result.append(temp_sum * str_length % mod)

    return sum(result) % mod


pre_l = str(int(L) - 1)

zero_to_left = zero_to_n_count(pre_l)
zero_to_right = zero_to_n_count(R)
left_int = zero_to_left
right_int = zero_to_right

# print(right_int)
# print(left_int)
print(int(right_int - left_int) % mod)