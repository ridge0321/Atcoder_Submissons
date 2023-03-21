N = int(input())
MAX_LEN = 1501

grid = [[0] * MAX_LEN for _ in range(MAX_LEN)]

for _ in range(N):
    X, Y = map(int, input().split())
    grid[X][Y] += 1


for y in range(1, MAX_LEN):
    for x in range(1, MAX_LEN):
        grid[x][y] += grid[x - 1][y]

for x in range(1, MAX_LEN):
    for y in range(1, MAX_LEN):
        grid[x][y] += grid[x][y - 1]


Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())

    ans = grid[c][d] - (grid[c][b - 1] + grid[a - 1][d]) + grid[a - 1][b - 1]

    print(ans)
