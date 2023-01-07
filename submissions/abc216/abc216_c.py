n = int(input())

ans_l = []
for i in range(120):
    if n % 2 == 0:
        n //= 2
        ans_l.append("B")
    else:
        n -= 1
        ans_l.append("A")

    if n == 0:
        break

ans_l = reversed(ans_l)
ans = "".join(ans_l)
print(ans)

# count = 0
# for a in list(ans):
#     if a == "A":
#         count += 1
#     else:
#         count *= 2

# print(count)
