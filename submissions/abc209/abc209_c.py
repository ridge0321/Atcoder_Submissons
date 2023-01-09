N = int(input())
C = list(map(int, input().split()))
C.sort()

mod = 10**9 + 7
ans = 1
for i in range(len(C)):
    ans *= C[i] - i
    ans = ans % mod

print(ans % mod)
