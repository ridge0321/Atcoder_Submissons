x1, y1, x2, y2 = map(int, input().split())

x = x2 - x1
y = y2 - y1

print("%d %d %d %d" % (x2 - y, y2 + x, x1 - y, y1 + x))
