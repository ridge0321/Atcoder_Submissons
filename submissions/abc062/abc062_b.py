H, W = map(int, input().split())
a = [str(input()) for i in range(H)]

for i in range(W + 1):
    print("#", end="")
else:
    print("#")

for a_list in a:
    print("#", end="")
    print(a_list, end="")
    print("#")

for i in range(W + 2):
    print("#", end="")
