for tc in range(1,11) :

    N = int(input())

    arr = list(map(str, input()))

    stack = [0] * 1000
    top = -1
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

    susik = ""

    for x in arr:

        if x not in '(+-*/)':

            susik += x

        elif x == ")":

            while stack[top] != "(":

                susik += stack[top]
                top -= 1

            top -= 1

        else:

            if top == -1 or isp[stack[top]] < icp[x]:

                top += 1
                stack[top] = x

            elif isp[stack[top]] >= icp[x]:

                while top > -1 and isp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1

                top += 1
                stack[top] = x
    susik += stack.pop(0)
    for x in susik:
        if x not in '+-/*':  # 피연산자면...
            top += 1  # push(x)
            stack[top] = int(x)
        else:
            op2 = stack[top]  # pop()
            top -= 1
            op1 = stack[top]  # pop()
            top -= 1
            if x == '+':  # op1 + op2
                top += 1  # push()
                stack[top] = op1 + op2
            elif x == '-':
                top += 1
                stack[top] = op1 - op2
            elif x == '/':
                top += 1
                stack[top] = op1 / op2
            elif x == '*':
                top += 1
                stack[top] = op1 * op2

    print(susik)
    print(stack)
    print(f"#{tc} {stack[top]}")