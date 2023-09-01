from collections import deque

T = int(input())

def bfs(N,M) :

    # 큐 생성
    # 시작점 인큐
    # visited 생성
    # 시작점 표시

    q = deque()

    visited = [[-1] * M for _ in range(N)]

    for i in range(N) :

        for j in range(M) :

            if arr[i][j] == 'W' :

                q.append((i,j))
                visited[i][j] = 0

    while q :

        i,j = q.popleft()

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]] :

            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'L' and visited[ni][nj] == -1 :

                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

    s = 0

    for i in range(N) :

        for j in range(M) :

            s += visited[i][j]

    return s

for tc in range(1,T+1) :

    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    print(f"#{tc} {bfs(N,M)}") # 육지에서 물에 도착하는 최단 거리의 합