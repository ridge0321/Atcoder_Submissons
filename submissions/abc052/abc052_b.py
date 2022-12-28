N = int(input())
S = list(str(input()))

x = 0
x_log = [0]

for s in S:
    if s == "I":
        x += 1
    else:
        x -= 1
    x_log.append(x)

print(max(x_log))
