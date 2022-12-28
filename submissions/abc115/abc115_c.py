N, K = map(int, input().split())
h = sorted([int(input()) for i in range(N)])

h_memo = []
for i in range(N - K + 1):
    h_min = h[i]
    h_max = h[i + K - 1]
    h_memo.append(h_max - h_min)

print(min(h_memo))
