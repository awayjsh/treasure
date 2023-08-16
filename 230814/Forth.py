T = int(input())

def forth(arr) :

    stack = []

    for i in arr:

        if i.isnumeric():

            stack.append(i)

        elif i == ".":

            break

        else:

            if len(stack) >= 2:

                n2 = int(stack.pop())
                n1 = int(stack.pop())
                ans = 0

                if i == "+":

                    ans = n1 + n2

                elif i == "-":

                    ans = n1 - n2

                elif i == "*":

                    ans = n1 * n2

                elif i == "/":

                    ans = n1 // n2

                stack.append(ans)

            else:

                print(f"#{tc} error")
                return

    if len(stack) != 1 :

        print(f"#{tc} error")
        return

    print(f"#{tc} {stack[0]}")
    return

for tc in range(1,T+1) :

    arr = list(map(str,input().split()))
    forth(arr)