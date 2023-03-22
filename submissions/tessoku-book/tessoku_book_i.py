H, W, N = map(int, input().split())

grid = [[0] * (W + 10) for _ in range(H + 10)]
grid_cum = [[0] * (W + 10) for _ in range(H + 10)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    grid[C + 1][D + 1] += 1
    grid[A][B] += 1
    grid[C + 1][B] -= 1
    grid[A][D + 1] -= 1

for h in range(1, H + 1):
    for w in range(1, W + 1):
        grid_cum[h][w] = grid_cum[h][w - 1] + grid[h][w]

for w in range(1, W + 1):
    for h in range(1, H + 1):
        grid_cum[h][w] += grid_cum[h - 1][w]


for h in range(1, H + 1):
    for w in range(1, W + 1):
        print(grid_cum[h][w], end="")
        if not (w == W):
            print(" ", end="")
    else:
        print("")
