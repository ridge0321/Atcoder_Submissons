W = list(str(input()))

count = {}

for w in W:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

for w_c in count.values():
    if w_c % 2 == 1:
        print("No")
        break
else:
    print("Yes")
