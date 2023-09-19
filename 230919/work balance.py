T = int(input())

def f(cnt,sum) :

    global max_v

    if max_v >= sum :

        return

    if cnt == N :

        if max_v <= sum :

            max_v = sum

    for num in idx :

        if num in path :

            continue

        path[cnt] = num

        f(cnt + 1, sum * (arr[cnt][path[cnt]-1]/100))

        path[cnt] = 0

for tc in range(1,T+1) :

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    idx = [i for i in range(1,N+1)]
    path = [0] * N
    max_v = 0
    f(0,1)

    new_ans = "{:.6f}".format(max_v * 100)

    print(f"#{tc} {new_ans}")