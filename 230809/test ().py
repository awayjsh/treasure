T = int(input())

for tc in range (1,T+1) :

    N = list(map(str,input()))

    stack = [0] * len(N)
    top = -1

    for i in range(len(N)) :

        if N[i] == "(" or N[i] == "{" :

            top += 1
            stack[top] = N[i]

        if N[i] == ")" or N[i] == "}" :

            top += 1
            stack[top] = N[i]

        if stack[top] == "}" and stack[top - 1] == "{" :

            stack[top] = 0
            top -= 1
            stack[top] = 0
            top -= 1

        if stack[top] == ")" and stack[top - 1] == "(" :

            stack[top] = 0
            top -= 1
            stack[top] = 0
            top -= 1

    if stack[0] != 0 :

        print(f"#{tc} 0")

    else :

        print(f"#{tc} 1")