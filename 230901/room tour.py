T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    room = [list(map(int, input().split())) for _ in range(N)]

    di = [0,0,-1,1]
    dj = [1,-1,0,0]

    ans = []

    for i in range(N) :

        for j in range(N) :

            start_i = i
            start_j = j
            count = 0
            is_find = False

            while True :

                for k in range(4) :

                    ni = start_i + di[k]
                    nj = start_j + dj[k]

                    if 0 <= ni < N and 0 <= nj < N and room[ni][nj] == room[start_i][start_j] + 1 :

                        count = count + 1
                        start_i = ni
                        start_j = nj
                        is_find = True

                if is_find == False:

                    break

                is_find = False

            ans.append([count, room[i][j]])

    max_v = 0
    room_number = 1e9

    for i in ans :

        if max_v < i[0] :

            max_v = i[0]
            room_number = i[1]

        if max_v == i[0] :

            if room_number > i[1] :

                room_number = i[1]

    print(f"#{tc} {room_number} {max_v + 1}")