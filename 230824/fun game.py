T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [[''] * (N+1) for _ in range(N+1)]
    di = [0, 0, 1, -1, 1, -1, 1, -1]
    dj = [1, -1, 0, 0, 1, -1, -1, 1]

    for i in range(N//2, N//2 + 2):
        for j in range(N//2, N//2 + 2):
            if i == j:
                lst[i][j] = 'W'
            else:
                lst[i][j] = 'B'

    for _ in range(M):

        i, j, color = map(int, input().split())

        if color == 1:
            lst[i][j] = 'B'
        else:
            lst[i][j] = 'W'

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 < ni <= N and 0 < nj <= N:
                if lst[ni][nj] != lst[i][j] and lst[ni][nj] != '':
                    stack = []
                    stack.append([ni, nj])

                    while True:
                        now_color = lst[i][j]

                        ni = ni + di[k]
                        nj = nj + dj[k]

                        if 0 < ni <= N and 0 < nj <= N:
                            if lst[ni][nj] != lst[i][j] and lst[ni][nj] != '':
                                stack.append([ni, nj])

                            elif lst[ni][nj] == lst[i][j] :
                                break

                            elif lst[ni][nj] == "" :

                                stack = []
                                break
                        else:
                            stack = []
                            break

                    for coords in stack:
                        x, y = coords[0], coords[1]

                        if color == 1:
                            lst[x][y] = 'B'
                        else:
                            lst[x][y] = 'W'

    B_count = 0
    W_count = 0

    for i in range(1,N+1) :

        for j in range(1,N+1) :

            if lst[i][j] == "B" :

                B_count += 1

            if lst[i][j] == 'W' :

                W_count += 1

    print(f"#{tc} {B_count} {W_count}")
