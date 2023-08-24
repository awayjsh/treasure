T = int(input())

for tc in range(1,T+1) :

    input_arr = list(input().split())

    num = [i for i in input_arr[1]]

    N = int(input_arr[0])

    for i in range(N) :

        change = int(num[i],16)
        b = format(change,'b')
        num[i] = b

    print(f"#{tc} ",end = "")

    while num :

        n = num.pop(0)

        if len(n) != 4 :

            M = 4 - len(n)

            for i in range(M) :

                print(0,end = "")

        print(n,end = "")

    print()


