# T = int(input())
#
# for tc in range(1,T+1) :
#
#     N, M = map(int, input().split())
#
#     cnt = 0
#
#     min_v = 1e9
#
#     stack = [(N,cnt)]
#
#     while stack :
#
#         print(stack)
#
#         now,now_cnt = stack.pop(0)
#
#         if now_cnt > min_v :
#
#             continue
#
#         if now == M :
#
#             if min_v >= now_cnt :
#
#                 min_v = now_cnt
#
#         else :
#             now_cnt += 1
#             stack.append((now + 1, now_cnt))
#             stack.append((now - 1, now_cnt))
#             stack.append((now * 2, now_cnt))
#             stack.append((now - 10, now_cnt))
#
#     print(f"#{tc} {min_v}")


from collections import deque

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    MAX_NUM = 1000000

    queue = deque([(N, 0)])
    min_ops = [1e9] * (MAX_NUM + 1)
    min_ops[N] = 0

    while queue:
        num, cnt = queue.popleft()

        if cnt > min_ops[num]:
            continue

        if num == M:
            min_v = cnt
            break

        for next_num in [num+1, num-1, num*2, num-10]:
            if 1 <= next_num <= MAX_NUM and cnt + 1 < min_ops[next_num]:
                queue.append((next_num,cnt+1))
                min_ops[next_num] = cnt + 1

    print(f"#{tc} {min_v}")

