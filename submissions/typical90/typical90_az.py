N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

s = 1
for a in A:
    s *= sum(a)

print(s % (10**9 + 7))
