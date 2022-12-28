A, B = map(int, input().split())

for i in range(1, 100001):
    tax_eight = int(i * 0.08)
    tax_ten = int(i * 0.1)

    if A == tax_eight and B == tax_ten:
        print(i)
        break
else:
    print(-1)
