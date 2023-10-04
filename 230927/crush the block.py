T = int(input())

for tc in range(1,T+1) :

    N,W,H = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(H)]
    new_arr = []
    visited = [[0] * H for _ in range(W)]

    for i in range(W) :

        part_lst = []

        for j in range(H) :

            part_lst.append(arr[j][i])

        new_arr.append(part_lst)

    di = [0,0,-1,1]
    dj = [1,-1,0,0]

    for i in range(W) :

        for j in range(H) :

            if new_arr[i][j] == 1 :

                for n in range(4) :

                    for k in range(0,new_arr[i][j])

                        ni = i + di[n] * k
                        nj = j + dj[n] * k

                        if 0 <= ni < N and 0 <= nj < N :

                            stack.append((ni,nj))
                            visited[ni][nj] = 1

                break