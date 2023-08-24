for tc in range(1,11) :

    N = int(input())

    H = [0] * (N+1)

    arr = [list(map(str, input().split())) for _ in range(N)]

    for i in reversed(arr) :

        if i[1].isdigit() :

            H[int(i[0])] = int(i[1])

        else :

            if i[1] == '+' :

                H[int(i[0])] = H[int(i[2])] + H[int(i[3])]

            elif i[1] == '-' :

                H[int(i[0])] = H[int(i[2])] - H[int(i[3])]

            elif i[1] == '*' :

                H[int(i[0])] = H[int(i[2])] * H[int(i[3])]

            elif i[1] == '/' :

                H[int(i[0])] = H[int(i[2])] / H[int(i[3])]

    print(f"#{tc} {int(H[1])}")