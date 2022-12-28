X = int(input())

max_bp = 1
for b in range(1, X):
    for p in range(2, 10):
        if b**p <= X:
            max_bp = max(max_bp, b**p)

print(max_bp)
