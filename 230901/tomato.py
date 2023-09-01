from collections import deque

M, N = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

q = deque()

visited = [[0] * M for _ in range(N)]

is_break = False

for i in range(N) :

    for j in range(M) :

        if arr[i][j] == 1 :

            q.append((i,j))
            visited[i][j] = 1

count = 0

while q :

    i,j = q.popleft()

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:

        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < M :

            if arr[ni][nj] == 0 and visited[ni][nj] == 0 :

                arr[ni][nj] = 1
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

max_v = 0

for i in range(N) :

    for j in range(M) :

        if visited[i][j] == 0 and arr[i][j] == -1 :

            continue

        if visited[i][j] == 0 and arr[i][j] == 0 :

            is_break = True
            break

        if max_v <= visited[i][j] :

            max_v = visited[i][j]

    if is_break :

        break

if is_break :

    print(-1)

else :

    print(max_v - 1)

