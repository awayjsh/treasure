T = int(input())

def dfs(i,j,N) :

    stack = []
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while True :

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]] :

            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and visited[ni][nj] == 0 :

                stack.append((i,j))
                i,j = ni,nj
                visited[i][j] = 1
                break

            elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 3 and visited[ni][nj] == 0:

                return 1




        else :

            if stack :

                i,j = stack.pop()

            else :

                break

    return 0

    # if len(stack) == 0 :
    #
    #     return 0

for tc in range(1,T+1) :

    N = int(input())

    arr = [list(map(int,input())) for _ in range(N)]

    for i in range(N) :

        for j in range(N) :

            if arr[i][j] == 2 :

                start = i
                end = j
                break

        if arr[i][j] == 2 :

            break

    result = dfs(start,end,N)
    print(f"#{tc} {result}")

