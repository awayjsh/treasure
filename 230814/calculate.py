'''
(6+5*(2-8)/2)
6528-*2/+
'''
stack = [0]*100
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = '9+5*2+1+3*3*7*6*9*1*7+1+8*6+6*1*1*5*2*4*7+4*3*8*2*6+7*8*4*5+3+7+2+6+5+1+7+6+7*3*6+2+6+6*2+4+2*2+4*9*3'
susik = ''
for x in fx:
    if x not in '(+-*/)':   # 피연산자
        susik += x
    elif x == ')':      # '('까지 pop()
        while stack[top] != '(':    # peek
            susik += stack[top]
            top -= 1
        top -= 1        # '(' 버림. pop
    else:   # '(+-*/'
        if top==-1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
            top += 1    # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1  # push
            stack[top] = x

print(susik)

#susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*': # 피연산자면...
        top += 1            # push(x)
        stack[top] = int(x)
    else:
        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1
        if x=='+':  # op1 + op2
            top += 1                # push()
            stack[top] = op1 + op2
        elif x=='-':
            top += 1
            stack[top] = op1 - op2
        elif x=='/':
            top += 1
            stack[top] = op1 / op2
        elif x=='*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])
print(stack)