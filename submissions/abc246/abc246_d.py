
def f(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


N = int(input())

ans_list = []


for b in range(0, 10**6 + 1):
    l = 0
    r = 10**6

    while 1 < r - l:
        center = (l + r) // 2

        if f(center, b) == N:
            print(N)
            quit()

        elif f(center, b) > N:
            r = center
        else:
            l = center
    else:
        if f(l, b) >= N:
            ans_list.append(f(l, b))
        else:
            ans_list.append(f(r, b))

ans = min(ans_list)

print(ans)
