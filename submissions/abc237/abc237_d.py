from collections import deque

N = int(input())
S = list(str(input()))

dq = deque()
dq.append(N)

for i in reversed(range(N)):
    if S[i] == "L":
        dq.append(i)
    else:
        dq.appendleft(i)
ans = list(dq)
print(*ans)
