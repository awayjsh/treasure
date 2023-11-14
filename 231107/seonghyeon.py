def bfs(V) :

    visit = [[0] for _ in range(V+2)]
    
    for i in range(len(arr)) :

        visit[arr[i] + 1] += 1

    while q :

        t = q.pop(0)

        if adj[t] != 'null' :

            if visit[adj[t]]



    
N = int(input())
arr = list(map(int,input().split()))

V = max(arr)

adj = {}

for i in range(V) :

    adj[i] = 'null'

for i in range(len(arr)) :

    if arr[i] == -1 :

        continue

    else :

        if arr[i] > arr[i-1] :

            adj[arr[i-1]] = arr[i]

print(adj)

# bfs(V)
