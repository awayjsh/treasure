#
#
# from itertools import permutations
#
# T = int(input())
#
# def all_permutations(lst) :
#
#     ans = []
#
#     for perm in permutations(lst) :
#
#         ans.append(perm)
#
#     return ans
#
# def calculate(num, i):
#
#     j = 0
#     stack = []
#     i = list(i)
#
#     while True :
#
#         if len(stack) == 0 :
#             stack.append(num[j])
#             j += 1
#             continue
#
#         stack.append(i.pop(0))
#         stack.append(num[j])
#         j += 1
#
#         if len(stack) == 3 :
#
#             a = stack.pop(0)
#             b = stack.pop(0)
#             c = stack.pop(0)
#
#             # print(a,b,c)
#
#             if b == '+' :
#
#                 stack.append(a+c)
#
#             elif b == '-' :
#
#                 stack.append(a-c)
#
#             elif b == '*' :
#
#                 stack.append(a*c)
#
#             elif b == '/' :
#
#                 stack.append(int(a/c))
#
#         if len(i) == 0 :
#
#             break
#
#     return stack[0]
#
# for tc in range(1,T+1) :
#
#     N = int(input())
#
#     cal = list(map(int,input().split()))
#
#     num = list(map(int,input().split()))
#
#     match = ['+','-','*','/']
#
#     result = []
#
#     all_match = []
#
#     max_v = -1e9
#     min_v = 1e9
#
#     for i in range(len(cal)) :
#
#         for j in range(cal[i]) :
#
#             result.append(match[i])
#
#     all_match = all_permutations(result)
#
#     min_result = float('inf')
#     max_result = float('-inf')
#
#     for i in all_match :
#
#         result = calculate(num,i)
#
#         min_result = min(min_result, result)
#         max_result = max(max_result, result)
#
#     print(f"#{tc} {max_result - min_result}")
#
#
#
#
T = int(input())


def calculate(num, operators):
    result = num[0]
    for i in range(1, len(num)):
        if operators[i - 1] == '+':
            result += num[i]
        elif operators[i - 1] == '-':
            result -= num[i]
        elif operators[i - 1] == '*':
            result *= num[i]
        elif operators[i - 1] == '/':
            if result < 0:
                result = -(-result // num[i])
            else:
                result //= num[i]

    return result


def backtrack(num, operators):
    global max_diff
    global min_diff
    if len(operators) == N - 1:
        res = calculate(num[:], operators[:])
        max_diff = max(max_diff, res)
        min_diff = min(min_diff, res)
        return

    for op in ['+', '-', '*', '/']:
        if operator_count[op] > 0:
            operator_count[op] -= 1
            operators.append(op)
            backtrack(num[:], operators[:])
            operator_count[op] += 1
            operators.pop()


for tc in range(1, T + 1):
    N = int(input())

    operator_count = {'+': 0, '-': 0, '*': 0, '/': 0}

    counts = list(map(int, input().split()))

    numbers = list(map(int, input().split()))

    # 연산자 카드 개수 세기
    for i in range(4):
        operator_count['+-*/'[i]] += counts[i]

    max_diff = float('-inf')
    min_diff = float('inf')
    backtrack(numbers[:], [])

    print(f"#{tc} {max_diff - min_diff}")


