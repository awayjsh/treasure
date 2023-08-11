def dfs(n,v,adj_m) :

    stack = []
    visited = [0] * (v+1)
    visited[n] = 1
    ans = []
    ans.append(n)

    while True :

        for w in range(1,v+1) :

            if adj_m[n][w] == 1 and visited[w] == 0 :

                stack.append(n)
                n = w
                ans.append(n)
                visited[n] = 1
                break

        else :

            if stack :

                n = stack.pop()

            else :

                break

    return set(ans)

v,e = map(int, input().split())
adj_m = [[0] * (v+1) for _ in range(v+1)]
ans = []

for i in range(e) :

    v1, v2 = map(int, input().split())

    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

for i in range(1,v+1) :

    new = dfs(i,v,adj_m)

    if new not in ans :

        ans.append(new)

print(len(ans))





