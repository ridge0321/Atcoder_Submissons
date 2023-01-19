N = int(input())
# 長方形の左下の頂点を１　右下２　左上３　右上４とする

xy_list = []
# 横並び
y_key_x_list_value = {}
# 縦並び
x_key_y_list_value = {}

for i in range(N):
    x, y = map(int, input().split())
    xy_list.append([x, y])

    if y not in y_key_x_list_value:
        y_key_x_list_value[y] = [x]
    else:
        y_key_x_list_value[y].append(x)

    if x not in x_key_y_list_value:
        x_key_y_list_value[x] = [y]
    else:
        x_key_y_list_value[x].append(y)

# print(xy_list)
# print(x_key_y_list_value)
# print(y_key_x_list_value)
count = 0
for xy in xy_list:
    x1 = xy[0]
    y1 = xy[1]

    y2 = y1
    x3 = x1

    for x2 in y_key_x_list_value[y1]:
        if x2 == x1:
            continue
        for y3 in x_key_y_list_value[x1]:
            if y3 == y1:
                continue
            if y3 in x_key_y_list_value[x2]:
                count += 1

print(count // 4)
