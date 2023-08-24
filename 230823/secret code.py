T = int(input())

# dic = { : 0, : 1, : 2,  : 3,  : 4, :5, : 6, : 7, : 8, : 9}

for tc in range(1,T+1) :

    N, M = map(int,input().split())

    arr = [list(map(int, input())) for _ in range(N)]

    end_i, end_j = 0, 0

    for i in reversed(range(N)) :

        for j in reversed(range(M)) :

            if arr[i][j] == 1 :

                end_i = i
                end_j = j

                break

        if end_i != 0 and end_j != 0 :

            break

    secret_code = []
    ans = []

    for j in range(end_j - 55, end_j + 1) :

        secret_code.append(arr[i][j])

    for i in range(0,50,7) :

        n = secret_code[i:i+7]

        if n == [0,0,0,1,1,0,1] :

            ans.append(0)

        elif n == [0,0,1,1,0,0,1] :

            ans. append(1)

        elif n == [0,0,1,0,0,1,1]:

            ans.append(2)

        elif n == [0,1,1,1,1,0,1]:

            ans.append(3)

        elif n == [0,1,0,0,0,1,1]:

            ans.append(4)

        elif n == [0,1,1,0,0,0,1]:

            ans.append(5)

        elif n == [0,1,0,1,1,1,1]:

            ans.append(6)

        elif n == [0,1,1,1,0,1,1]:

            ans.append(7)

        elif n == [0,1,1,0,1,1,1]:

            ans.append(8)

        elif n == [0,0,0,1,0,1,1]:

            ans.append(9)


    real_ans = 0

    for i in range(len(ans)) :

        if (i+1) % 2 != 0 :

            real_ans = real_ans + ans[i] * 3

        else :

            real_ans = real_ans + ans[i]

    if real_ans % 10 == 0 :

        total = 0

        for i in ans :

            total = total + i

        print(f"#{tc} {total}")

    else :

        print(f"#{tc} 0")
