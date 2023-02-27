D = int(input())
N = int(input())

io = [0] * (10**5)
cum = [0]

for _ in range(N):
    L, R = map(int, input().split())
    io[L] += 1
    io[R + 1] -= 1

# print(io)

for i in range(1, len(io)):
    cum.append(cum[i - 1] + io[i])

# print(cum)

for i in range(1, D + 1):
    print(cum[i])
