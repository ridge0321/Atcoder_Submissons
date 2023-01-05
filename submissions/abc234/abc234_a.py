t = int(input())


def f(x):
    res = x**2 + 2 * x + 3
    return res


result = f(f(f(t) + t) + f(f(t)))

print(result)
