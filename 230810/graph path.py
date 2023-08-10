def dfs(n, V, adj_m, G) :

    is_in = False
    stack = []
    visited = [0] * (V+1)
    visited[n] = 1

    if n == G :

        is_in = True

    while True :

        for w in range(1, V+1) :

            if adj_m[n][w] == 1 and visited[w] == 0:

                stack.append(n)
                n = w

                if n == G :

                    is_in = True

                visited[n] = 1
                break

        else :

            if stack :

                n = stack.pop()

            else :

                break

    return is_in

T = int(input())

for tc in range(1,T+1) :

    V, E = map(int, input().split())
    adj_m = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E) :

        v1, v2 = map(int, input().split())

        adj_m[v1][v2] = 1

    S, G = map(int, input().split())

    if dfs(S, V, adj_m, G) :

        print(f"#{tc} 1")

    else :

        print(f"#{tc} 0")