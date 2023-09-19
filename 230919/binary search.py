T = int(input())

def isbinarySearch(target) :

    low = 0
    high = len(lst_1)-1
    mid_count = 0
    left_count = 0
    right_count = 0
    stack = []
    is_not = True

    while low <= high :

        mid = (low + high) // 2

        if lst_1[mid] == target :

            mid_count += 1

            break

        elif lst_1[mid] < target :

            right_count += 1

            stack.append('R')

            if len(stack) >= 2 and stack[-1] == stack[-2] :

                is_not = False

            low = mid + 1

        else :

            left_count += 1

            stack.append('L')

            if len(stack) >= 2 and stack[-1] == stack[-2] :

                is_not = False

            high = mid - 1

    if is_not == False :

        return 0

    if mid_count == 1 :

        if right_count == left_count or abs(right_count - left_count) == 1 :

            return 1

    else :

        return 0



for tc in range(1,T+1) :

    N, M = map(int,input().split())

    lst_1 = list(map(int,input().split()))
    lst_1.sort()
    lst_2 = list(map(int,input().split()))
    cnt = 0

    for i in lst_2 :

        if isbinarySearch(i) :

            cnt += 1

    print(f"#{tc} {cnt}")