import sys

sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
C = [list(str(input())) for i in range(H)]

visit = [[False] * W for i in range(H)]


def dfs(x, y):
    if x > W - 1 or x < 0 or y > H - 1 or y < 0:
        return
    if C[y][x] == "#":
        return
    if visit[y][x] == True:
        return

    visit[y][x] = True

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


for i in range(H):
    for j in range(W):
        if C[i][j] == "s":
            start_x = j
            start_y = i
        if C[i][j] == "g":
            goal_x = j
            goal_y = i

dfs(start_x, start_y)

if visit[goal_y][goal_x] == True:
    ans = "Yes"
else:
    ans = "No"

print(ans)
