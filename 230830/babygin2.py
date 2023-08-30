def f(AorB,i,N,K) :

    global is_ans

    if i == K :

        if p[0] == p[1] == p[2] or p[0] + 1 == p[1] == p[2] - 1 :

            if is_ans == 0 :

                is_ans = AorB

            return



    else :

        for j in range(N) :

            if used[j] == 0 :

                if AorB == 1 :

                    p[i] = A[j]
                    used[j] = 1
                    f(1,i+1,N,K)
                    used[j] = 0

                elif AorB == 2 :

                    p[i] = B[j]
                    used[j] = 1
                    f(2,i+1,N,K)
                    used[j] = 0

T = int(input())

for tc in range(1,T+1) :

    card = list(map(int,input().split()))
    A = []
    B = []
    is_ans = 0

    for i in range(len(card)) :

        if i % 2 == 0 :

            A.append(card[i])

            if len(A) >= 3 :

                N = len(A)
                used = [0] * N
                p = [0] * 3
                f(1,0,N,3)

        elif i % 2 == 1 :

            B.append(card[i])

            if len(B) >= 3 :

                N = len(B)
                used = [0] * N
                p = [0] * 3
                f(2,0,N,3)

        elif is_ans != 0 :

            break

    print(f"#{tc} {is_ans}")
