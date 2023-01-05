X = int(input())

if X >= 90:
    ans = "expert"
elif X >= 70:
    ans = 90 - X
elif X >= 40:
    ans = 70 - X
else:
    ans = 40 - X

print(ans)
