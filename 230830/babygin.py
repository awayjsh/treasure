T = int(input())

def f(i,N) :

    global is_ans

    if i == N :

        ans_count = 0

        if p[0:4][0] == p[0:4][1] == p[0:4][2] or p[0:4][0] == p[0:4][1] - 1 == p[0:4][2] - 2 :

            ans_count += 1

        if p[3:6][0] == p[3:6][1] == p[3:6][2] or p[3:6][0] == p[3:6][1] - 1 == p[3:6][2] - 2 :

            ans_count += 1

        if ans_count == 2 :

            is_ans = True
            return

    else :

        for j in range(N) :

            if used[j] == 0 :

                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

for tc in range(1,T+1) :

    card = list(map(int,input()))
    used = [0] * 6
    p = [0] * 6
    ans = []
    is_ans = False


    f(0,6)

    if is_ans == True :

        print(f"#{tc} Baby Gin")

    else :

        print(f"#{tc} Lose")

