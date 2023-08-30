T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    i = 0
    j = 0
    visited[i][j] = 1
    stack = []
    stack.append([i,j])

    di = [0,1]
    dj = [1,0]
    is_break = False

    while True :

        i,j = stack.pop(0)
        min = 1e9

        for k in range(2) :

            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 :

                min_part = arr[ni][nj]

                if 0 <= ni + 1 < N :

                    min_part += arr[ni+1][nj]

                if 0 <= nj + 1 < N :

                    min_part += arr[ni][nj+1]

                if min >= min_part :

                    min = min_part
                    new_i = ni
                    new_j = nj

        arr[new_i][new_j] = arr[new_i][new_j] + arr[i][j]

        if visited[new_i][new_j] == 0 :

            visited[new_i][new_j] = 1
            stack.append([new_i,new_j])

        if new_i == N-1 and new_j == N-1 :

            break

        if len(stack) == 0 :

            break

    for i in arr :

        print(i)

    print(f"#{tc} {arr[N-1][N-1]}")

