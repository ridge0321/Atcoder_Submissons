import math

N = int(input())

count = 0
for a in range(1, N + 1):
    if N < a**3:
        break

    for b in range(a, N + 1):
        if a * b * b > N:
            break

        # Cの取りうる範囲をカウント
        count += (N // (a * b)) - b + 1

print(count)
