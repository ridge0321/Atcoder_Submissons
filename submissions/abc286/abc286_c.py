N, A, B = map(int, input().split())
S = list(str(input()))
result = []
for i in range(N):
    first = S[i:]
    second = S[0:i]
    array = first + second
    a_count = i
    cost = 0

    for i in range(N // 2):
        if not (array[i] == array[-(i + 1)]):
            cost += B
    else:
        cost += a_count * A

    result.append(cost)

print(min(result))
