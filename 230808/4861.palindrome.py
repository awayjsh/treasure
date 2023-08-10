T = int(input())

for tc in range(1,T+1) :

    N, M = map(int,input().split())

    arr = [list(map(str,input())) for _ in range(N)]

    for i in arr :

        for j in range(0, N-M+1) :

            part = []

            for k in range(j, j+M) :

                part.append(i[k])

        if part == part[::-1] :

            part = "".join(part)
            print(f"#{tc} {part}")
            break

    new_arr = []

    for i in range(N) :

        part = []

        for j in range(N) :

            part.append(arr[j][i])

        new_arr.append(part)

    for i in new_arr :

        for j in range(0, N-M+1) :

            part = []

            for k in range(j, j+M) :

                part.append(i[k])

        if part == part[::-1] :

            part = "".join(part)
            print(f"#{tc} {part}")
            break