N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A)
sorted_B = sorted(B)

greedy_l = []

for i in range(N):
    greedy_l.append(abs(sorted_A[i] - sorted_B[i]))

print(sum(greedy_l))
