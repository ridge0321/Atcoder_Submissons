import numpy as np

N, K = map(int, input().split())

n_8 = str(N)
for i in range(K):
    n_int = int(n_8, 8)
    n_9 = np.base_repr(n_int, base=9)
    n_9 = n_9.replace("8", "5")

    n_8 = str(n_9)

print(n_8)
