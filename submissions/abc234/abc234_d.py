import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

heap_que = P[:K]
heapq.heapify(heap_que)
result = heapq.heappop(heap_que)
print(result)

for i in range(K, N):
    heapq.heappush(heap_que, max(P[i], result))
    result = heapq.heappop(heap_que)
    print(result)
