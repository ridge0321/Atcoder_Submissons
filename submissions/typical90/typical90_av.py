N, K = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]


l = []

for i in range(N):
    l.append(AB[i][1])
    l.append(AB[i][0] - AB[i][1])


l = sorted(l)[::-1]

print(sum(l[0:K]))
