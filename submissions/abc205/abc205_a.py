A, B = map(int, input().split())

result = A * B / 100

if result == A * B // 100:
    result = A * B // 100
print(result)
