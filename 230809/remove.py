T = int(input())

for tc in range(1, T+1) :

    N = list(map(str, input()))

    stack = [0] * len(N)
    top = -1

    for i in range(len(N)) :

        top += 1
        stack[top] = N[i]

        if stack[top] == stack[top - 1] :

            stack[top] = 0
            top -= 1
            stack[top] = 0
            top -= 1

    count = 0

    for i in stack :

        if i != 0 :

            count = count + 1

    print(f"#{tc} {count}")