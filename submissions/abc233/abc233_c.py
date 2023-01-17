N, X = map(int, input().split())
a = []
ans_count = 0
for i in range(N):
    La = list(map(int, input().split()))
    a.append(La[1:])

mul_result = [1]
for ai in a:
    temp_mul_result = []

    for m_r in mul_result:
        for i in range(len(ai)):
            temp_mul_result.append(ai[i] * m_r)

    mul_result = temp_mul_result

for m_r in mul_result:
    if m_r == X:
        ans_count += 1

print(ans_count)
