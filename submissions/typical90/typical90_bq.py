N, K = map(int, input().split())
mod = 10**9 + 7


def pow_calc(a, b):

    res = 1
    while b != 0:
        if b % 2 == 1:
            res = res * a % mod
        a = a * a % mod
        b = b // 2
    return res


if N == 1:
    ans = K % mod
elif N == 2:
    if K == 1:
        ans = 0
    else:
        ans = K * (K - 1) % mod
else:
    if K >= 3:
        ans = (K * (K - 1) * (pow_calc((K - 2), (N - 2)))) % mod
    else:
        ans = 0

print(ans)
