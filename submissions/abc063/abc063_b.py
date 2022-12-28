S = list(str(input()))

for s in S:
    if S.count(s) > 1:
        print("no")
        break
else:
    print("yes")
