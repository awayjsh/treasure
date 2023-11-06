def up(score,idx,stack) :

    global ans

    # print('score',score)
    # if len(stack) >= 3 :
    #     print('stack',stack[-1],stack[-2],stack[-3])

    if idx == N :

        ans = max(ans, score)
        return

    else :

        if idx + 1 <= N :

            stack.append(idx + 1)

            if len(stack) >= 3 and stack[-1] - 1 == stack[-2] == stack[-3] + 1 :

                stack.pop()

            else :

                up(score + arr[idx + 1],idx + 1,stack)
                stack.pop()

        if idx + 2 <= N :

            stack.append(idx + 2)

            up(score + arr[idx + 2],idx + 2,stack)
            stack.pop()


N = int(input())

arr = [0]

ans = 0

for _ in range(N) :

    arr.append(int(input()))

stack = [1]

up(arr[1],1,stack)

print(ans)
# print(stack)