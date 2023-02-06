class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1] * n

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


N, M = map(int, input().split())
ans = 0
plus_c_list = []

UF = UnionFind(N + 1)

for i in range(M):
    A, B, C = map(int, input().split())
    if C <= 0:
        UF.merge(A, B)
    else:
        ans += C
        plus_c_list.append([A, B, C])


plus_c_list.sort(key=lambda x: x[2])
for abc in plus_c_list:
    a = abc[0]
    b = abc[1]
    c = abc[2]
    if UF.size(1) == N:
        print(ans)
        quit()
    else:
        if not UF.same(a, b):
            UF.merge(a, b)
            ans -= c
else:
    print(ans)
