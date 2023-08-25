T = int(input())

for tc in range(1,T+1) :

    N, M = map(int,input().split())

    arr = [list(map(str,input())) for _ in range(N)]

    for i in range(N) :

        for j in range(M) :

            if arr[i][j] != 0 :

                change = int(arr[i][j], 16)
                b = format(change, 'b')
                arr[i][j] = b

    for i in arr :

        print("".join(i))