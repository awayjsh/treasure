for tc in range (1,11) :

    N = int(input())

    arr = [list(map(str, input())) for _ in range(8)]

    count = 0

    for i in arr:

        for j in range(0, 8-N+1):

            part = []

            for k in range(j, j + N):

                part.append(i[k])

            if part == part[::-1]:

                count = count + 1

    new_arr = []

    for i in range(8):

        part = []

        for j in range(8):

            part.append(arr[j][i])

        new_arr.append(part)

    for i in new_arr :

        for j in range(0, 8-N+1) :

            part = []

            for k in range(j, j+N) :

                part.append(i[k])

            if part == part[::-1] :

                count = count + 1

    print(f"#{tc} {count}")