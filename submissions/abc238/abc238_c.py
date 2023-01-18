N = int(input())
digit_n = len(str(N))
sum_fn_list = []
mod = 998244353


def sum_fn_top(num):
    # 引数の最大の桁でのf(n)の合計を返す
    calc_result = (num - (10 ** (digit_n - 1)) + 1) * (num - (10 ** (digit_n - 1)) + 1 + 1) // 2 % mod
    return calc_result


def sum_fn_other(i):
    # 引数の桁の中でのf(n)の合計値を返す
    calc_result = ((10**i - 1) - (10 ** (i - 1)) + 1) * ((10**i - 1) - (10 ** (i - 1)) + 1 + 1) // 2 % mod
    return calc_result


sum_fn_list.append(sum_fn_top(N))

if digit_n > 1:
    for i in range(1, digit_n):
        sum_fn_list.append(sum_fn_other(i))

ans = sum(sum_fn_list) % mod
print(ans)
