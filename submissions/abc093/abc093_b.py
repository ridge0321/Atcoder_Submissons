A, B, K = map(int, input().split())

small = A + K - 1
large = B - K + 1
ans_list = []

for i in range(A, A + K):
    if i > B:
        break
    ans_list.append(i)

for i in range(B - K + 1, B + 1):
    if i > A:
        ans_list.append(i)

result = sorted(list(set(ans_list)))

for i in result:
    print(i)
