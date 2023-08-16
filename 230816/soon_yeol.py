T = int(input())


def f(i,N,s) :

    global A
    global min_v

    if i == N :

        # total = 0

        # for i in range(N) :
        #
        #     total = total + arr[i][A[i]]

        if min_v >= s :

            min_v = s

    elif s >= min_v :

        return

    else :

        for j in range(i,N) : # 자신부터 오른쪽 끝까지

            A[i], A[j] = A[j], A[i]
            f(i+1,N, s + arr[i][A[i]])
            A[i], A[j] = A[j], A[i]

for tc in range(1,T+1) :

    N = int(input())

    min_v = 1e9

    arr = [list(map(int,input().split())) for _ in range(N)]

    A = [i for i in range(0,N)]

    s = 0

    f(0,N,s)

    print(f"#{tc} {min_v}")