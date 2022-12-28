a, b, c, K = map(int, input().split())


if K % 2 == 0:
    ans = a - b
else:
    ans = b - a

if abs(ans) > 10**18:
    ans = "Unfair"

print(ans)
