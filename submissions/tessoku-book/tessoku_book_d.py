N = int(input())
ans = []
for i in reversed(range(10)):
    ans.append((N // (2**i)) % 2)

for a in ans:
    print(str(a), end="")
print("")
