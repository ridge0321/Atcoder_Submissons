N = int(input())

GRID_LEN = 1510

grid = [[0] * GRID_LEN for _ in range(GRID_LEN)]
cum = [[0] * GRID_LEN for _ in range(GRID_LEN)]

for _ in range(N):
    A, B, C, D = map(int, input().split())

    grid[A][B] += 1
    grid[C][B] -= 1
    grid[A][D] -= 1
    grid[C][D] += 1

for h in range(0, GRID_LEN):
    for w in range(1, GRID_LEN):
        grid[h][w] += grid[h][w - 1]

for w in range(0, GRID_LEN):
    for h in range(1, GRID_LEN):
        grid[h][w] += grid[h - 1][w]

ans = 0

for h in range(GRID_LEN):
    for w in range(GRID_LEN):
        if grid[h][w] > 0:
            ans += 1

print(ans)
