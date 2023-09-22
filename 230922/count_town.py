T = int(input())

def dfs(now,cnt) :

    visited[now] = cnt

    for to in range(len(graph[now])) :

        next = graph[now][to]

        if visited[next] > 0 :

            continue

        dfs(next,cnt)

for tc in range(1,T+1) :

    N, M = map(int,input().split())

    visited = [0] * (N+1)

    graph = [[] for _ in range(N+1)]

    ans = 0

    for _ in range(M) :

        i,j = map(int,input().split())

        graph[i].append(j)
        graph[j].append(i)

    start = 1
    cnt = 0

    while True :

        if start == N + 1 :

            break

        if visited[start] == 0 :

            cnt += 1

            dfs(start,cnt)

        start += 1

    print(f"#{tc} {len(set(visited))-1}")

    # print(graph)

    # for i in graph :
    #
    #     if len(i) == 0 :
    #
    #         ans += 1
    #
    # ans += len(set(visited))-1
    #
    # print(f"#{tc} {ans - 1}")

    # cnt = 0
    # # 모든 정점을 순회하며 아직 방문하지 않은 정점에서 DFS 시작
    # for start in range(1, N + 1):
    #     if visited[start] == 0:
    #         cnt += 1
    #         dfs(start,cnt)
    #
    # print(f"#{tc} {cnt}")