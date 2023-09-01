from collections import deque

T = int(input())

def bfs(N,M) :

    q = deque()

    visited = [[0] * M for _ in range(N)]

    q.append((R,C))
    visited[R][C] = 1
    count = 0

    while q :

        i,j = q.popleft()

        count = count + 1

        for di, dj in route[arr[i][j]] :

            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] != 0 and visited[i][j] < L :

                if [-di, -dj] in route[arr[ni][nj]] :

                    q.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1

    return count

for tc in range(1,T+1) :

    N,M,R,C,L = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    route = [[],[[1, 0], [-1, 0], [0, 1], [0, -1]], [[1, 0], [-1, 0]], [[0, 1], [0, -1]],[[-1, 0], [0, 1]], [[1, 0], [0, 1]],[[1, 0], [0, -1]], [[-1, 0], [0, -1]]]

    print(f"#{tc} {bfs(N,M)}")
