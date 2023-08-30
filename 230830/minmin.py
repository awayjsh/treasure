def f(i,j,s,N) : # i,j : 현재 방문칸, s 이전에 지나온 칸의 숫자 합계

    global min

    if i >= N or j >= N :

        return

    elif i == N-1 and j == N-1 :

        if min >= s+arr[i][j] :

            min = s + arr[i][j]

    else :

        f(i,j+1,s + arr[i][j],N)
        f(i+1,j,s + arr[i][j],N)

T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    min = 1e9

    f(0,0,0,N)

    print(f"#{tc} {min}")