class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def _sum(self, r):
        s = 0
        while 0 < r:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def sum(self, l, r):
        r += 1
        return self._sum(r) - self._sum(l)

    def select(self, p):
        return self.sum(p, p)


N, Q = map(int, input().split())
a = list(map(int, input().split()))

fen = FenwickTree(N)

for i in range(N):
    fen.add(i, a[i])


for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 0:
        p = query[1]
        x = query[2]

        fen.add(p, x)

    else:
        l = query[1]
        r = query[2]

        print(fen.sum(l, r - 1))
