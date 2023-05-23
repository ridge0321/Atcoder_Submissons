N = int(input())

L = 1
R = 47
ans = None

for _ in range(20):
    M = (L + R) / 2

    fx = M**3 + M

    if fx > N:
        R = M
    else:
        L = M

else:
    ans = M

print(ans)
