S = list(str(input()))
K = int(input())
s_int_list = list(map(int, S))


for i in range(len(s_int_list)):
    if not (s_int_list[i] == 1) or K - 1 == i:
        print(s_int_list[i])
        break

# 100桁１の場合
# Kが
