# 이진탐색
def binary_search(A, N, t):
    low = 0
    high = N - 1
    cnt = 0
    stack = []
    flag = 0

    while low <= high:
        mid = (low + high) // 2
        cnt += 1
        if A[mid] == t:
            if cnt == 1:
                print(stack)
                return 1
            else:
                if len(stack) == 1 :
                    print(stack)
                    return 1

                for i in range(1,len(stack)):
                    if stack[i] != stack[i - 1]:
                        flag = 1
                        break
                    else:
                        flag = 0
                if flag == 1:
                    print(stack)
                    return 1
                else:
                    return 0

        elif A[mid] < t:

            low = mid - 1
            stack.append('R')

        else:
            high = mid + 1
            stack.append('L')

    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        if binary_search(A, N, b) == 1:
            ans += 1
    print(f'#{tc} {ans}')