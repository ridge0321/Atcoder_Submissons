N = int(input())
AB = [list(map(int, input().split())) for i in range(N)]
A = []
B = []
for ab in AB:
    A.append(ab[0])
    B.append(ab[1])

result = []
for i in range(N):
    start = A[i]
    for j in range(N):
        end = B[j]

        sum_sec = 0
        for ab in AB:
            a = ab[0]
            b = ab[1]
            a_to_b = abs(start - a) + abs(a - b) + abs(b - end)
            b_to_a = abs(start - b) + abs(b - a) + abs(a - end)
            sum_sec += min(a_to_b, b_to_a)

        result.append(sum_sec)

print(min(result))
