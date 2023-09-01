T = int(input())

for tc in range(1,T+1) :

    N, M = map(int,input().split())

    arr = [list(input()) for _ in range(N)]

    land = [[0] * M for _ in range(N)]

    for i in range(N) :

        for j in range(M) :

            if arr[i][j] == 'W' :

                land[i][j] = 1

            else :

                land[i][j] = 0

    di = [0,0,-1,1]
    dj = [1,-1,0,0]

    li = [1,1,-1,-1]
    lj = [-1,1,-1,1]

    for i in range(N) :

        for j in range(M) :

            if arr[i][j] == 'W' :

                for k in range(4) :

                    n = 0
                    start_i = i
                    start_j = j

                    while True :

                        ni = start_i + di[k]
                        nj = start_j + dj[k]

                        if 0 <= ni < N and 0 <= nj < M :

                            if arr[ni][nj] == "L" :

                                if  land[ni][nj] == 0 :

                                    n = n + 1
                                    land[ni][nj] = n
                                    start_i = ni
                                    start_j = nj

                                elif land[ni][nj] > 0 :

                                    n = n + 1
                                    land[ni][nj] = min(n, land[ni][nj])
                                    start_i = ni
                                    start_j = nj

                            elif arr[ni][nj] == 'W':

                                break

                        else :

                            break

                    ni = i + li[k]
                    nj = j + lj[k]

                    if 0 <= ni < N and 0 <= nj < M :

                        if arr[ni][nj] == 'L' :

                            if land[ni][nj] == 0 :

                                land[ni][nj] = 2

                            elif land[ni][nj] > 0 :

                                land[ni][nj] = min(land[ni][nj], 2)
    ans = 0

    for i in range(N) :

        for j in range(M) :

            if land[i][j] == 0 :

                min_v = 1000

                for k in range(4) :

                    ni = i + di[k]
                    nj = j + dj[k]

                    if 0 <= ni < N and 0 <= nj < M :

                        min_v = min(min_v,land[ni][nj])

                land[i][j] = min_v + 1

            if arr[i][j] == "L" :

                ans += land[i][j]

    print(f"#{tc} {ans}")