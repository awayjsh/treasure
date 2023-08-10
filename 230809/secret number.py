for tc in range(1,11) :

    N, num = map(str, input().split(" "))

    N = int(N)
    num = [int(i) for i in num]

    stack = ["-"] * N
    top = -1

    for i in range(N) :

        top += 1
        stack[top] = num[i]

        if stack[top] == stack[top-1] :

            stack[top] = "-"
            top -= 1
            stack[top] = "-"
            top -= 1

    print(f"#{tc} ",end = "")

    for i in stack :

        if i != "-" :

            print(i,end = "")

    print()