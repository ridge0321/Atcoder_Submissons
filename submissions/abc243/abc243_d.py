from collections import deque

N, X = map(int, input().split())
S = list(str(input()))

s_que = deque()
s_que.append("")
prev_s = ""
for s in S:
    if s == "U" and (prev_s == "R" or prev_s == "L"):
        s_que.pop()
        prev_s = s_que[-1]
    else:
        s_que.append(s)
        prev_s = s

s_que = list(s_que)[1:]


for s in s_que:
    if s == "U":
        X = X // 2
    elif s == "L":
        X = X * 2
    else:
        X = X * 2 + 1

print(X)
