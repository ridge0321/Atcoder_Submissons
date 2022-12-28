Q, H, S, D = map(int, input().split())
N = int(input())


q_cost = Q * 4 * N
h_cost = H * 2 * N
s_cost = S * N

over_cost = 0
if N % 2 == 1:
    over_cost = min(Q * 4, H * 2, S)

d_cost = over_cost + N // 2 * D

print(min(q_cost, h_cost, s_cost, d_cost))
