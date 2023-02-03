import copy
import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())


index_dict = {}
for i in range(1, N + 1):
    index_dict[i] = []


for i in range(N):
    index_dict[A[i]].append(i + 1)

# print(index_dict)

for i in range(Q):
    L, R, X = map(int, input().split())

    right_edge = bisect.bisect_right(index_dict[X], R)
    left_edge = bisect.bisect_left(index_dict[X], L)

    print(right_edge - left_edge)
