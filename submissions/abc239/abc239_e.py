import sys

readline = sys.stdin.readline
sys.setrecursionlimit(10**7)


def main():

    N, Q = map(int, readline().split())
    X = list(map(int, [-1] + readline().split()))
    AB = [list(map(int, readline().split())) for i in range(N - 1)]

    tree = [[] for _ in range(N + 1)]
    ans_list = [[]] * (N + 1)
    visited = [False] * (N + 1)
    visited[1] = True

    for ab in AB:
        a = ab[0]
        b = ab[1]
        tree[a].append(b)
        tree[b].append(a)

    def DFS(now_n_index):

        ans_list[now_n_index] = [X[now_n_index]]
        for next in tree[now_n_index]:
            if not visited[next]:
                visited[next] = True
                DFS(next)
                ans_list[now_n_index].extend(ans_list[next])

        ans_list[now_n_index].sort(reverse=True)
        ans_list[now_n_index] = ans_list[now_n_index][:20]

    DFS(1)
    # print(tree_dict)
    # print(ans_dict)

    for i in range(Q):
        V, K = map(int, readline().split())
        ans = ans_list[V][K - 1]
        print(ans)


main()
