T = int(input())

def f(cnt,sum) :

    global min_v

    if min_v < sum :

        return

    if cnt == N :

        if min_v >= sum :

            min_v = sum

        return

    for num in idx :

        if num in path :

            continue

        path[cnt] = num

        f(cnt + 1, sum + arr[cnt][path[cnt]-1])

        path[cnt] = 0

for tc in range(1,T+1) :

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    idx = [i for i in range(1,N+1)]
    path = [0] * N
    min_v = 1e9
    f(0,0)

    print(f"#{tc} {min_v}")