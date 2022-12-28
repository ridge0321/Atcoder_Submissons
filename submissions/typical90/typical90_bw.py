N = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


count = 0
sum_index = len(prime_factorize(N))
while sum_index > 1:
    if sum_index % 2 == 0:
        sum_index //= 2
    else:
        sum_index = sum_index // 2 + 1
    count += 1

print(count)
