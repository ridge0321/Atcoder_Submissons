T = int(input())
N = int(input())

io = [0] * (T + 10)


for _ in range(N):
    L, R = map(int, input().split())
    io[L] += 1
    io[R] -= 1

# print(io)

cum = [io[0]]

for i in range(1, len(io)):
    cum.append(cum[i - 1] + io[i])

# print(cum)

for i in range(T):
    print(cum[i])
