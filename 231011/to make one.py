T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = [list(map(int,input())) for _ in range(N)]

    di = [0,0,-1,1]
    dj = [1,-1,0,0]
    visited = []
    cnt = [[-1e9] * N for _ in range(N)]
    cnt[0][0] = 0
    visited.append((0,0))
    check = [[0] * N for _ in range(N)]

    while True :

        print(visited)
        i,j = visited.pop(0)
        check[i][j] = 1

        min = 1e9
        min_i = 0
        min_j = 0

        for k in range(4) :

            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and check[ni][nj] == 0:

                if min <= arr[ni][nj] + arr[i][j] :
                    min = arr[ni][nj] + arr[i][j]
                    min_i = ni
                    min_j = nj

        cnt[min_i][min_j] = min
        visited.append((min_i,min_j))
        check[min_i][min_j] = 1

        if len(visited) == 0 :

            break

    for i in cnt :

        print(i)

