N = int(input())
st = [list(input().split()) for i in range(N)]

for i in range(N):
    temp_s = st[i][0]
    st[i][0] = int(st[i][1])
    st[i][1] = temp_s

st = sorted(st, reverse=True)
print(st[1][1])
