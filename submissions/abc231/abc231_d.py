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
UF = UnionFind(N + 1)
graph_dict = {}

for i in range(1, N + 1):
    graph_dict[i] = []

for i in range(M):
    A, B = map(int, input().split())
    graph_dict[A].append(B)
    graph_dict[B].append(A)

    if UF.same(A, B) or len(graph_dict[A]) > 2 or len(graph_dict[B]) > 2:
        print("No")
        quit()
    else:
        UF.merge(A, B)
        
print("Yes")
