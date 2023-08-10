def dfs(n, V, adj_m) :

    stack = []
    visited = [0] * (V+1)
    visited[n] = 1
    ans = []
    ans.append(n)

    while True :

        for w in range(1,V+1) :

            if adj_m[n][w] == 1 and visited[w] == 0 :

                stack. append(n)
                n = w
                ans.append(n)
                visited[n] = 1
                break

        else :

            if stack :

                n = stack.pop()

            else :

                break

    if V in ans :

        return True

    else :

        return False




for i in range(1,11) :

    tc, path = map(int, input().split())

    arr = list(map(int, input().split()))

    adj_m = [[0] * (100) for _ in range(100)]

    for i in range(path) :

        v1, v2 = arr[i*2], arr[i*2+1]
        adj_m[v1][v2] = 1

    if dfs(0,99,adj_m) :

        print(f"#{tc} 1")

    else :

        print(f"#{tc} 0")