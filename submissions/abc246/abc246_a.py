xy = [list(map(int, input().split())) for i in range(3)]

x_l = []
y_l = []


for i in range(3):
    x_l.append(xy[i][0])
    y_l.append(xy[i][1])

for x in x_l:
    if x_l.count(x) == 1:
        ans_x = x

for y in y_l:
    if y_l.count(y) == 1:
        ans_y = y

print(ans_x, ans_y)
