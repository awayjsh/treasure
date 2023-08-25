for tc in range(1,11) :

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    is_N = False
    count = 0

    for i in range(N) :

        for j in range(N) :

            if arr[j][i] == 1 :

                is_N = True

            if is_N == True and arr[j][i] == 2 :

                count = count + 1
                is_N = False

        is_N = False

    print(f"#{tc} {count}")