# T = int(input())
#
# def find_food(cal, score, count,idx) :
#
#     global max_v
#
#     if count <= N and cal <= L:
#
#         if score >= max_v :
#
#             max_v = score
#
#     if cal > L :
#
#         return
#
#     if count > N :
#
#         return
#
#     else :
#
#         for i in range(len(food)) :
#
#             if idx[i] == 0 :
#
#                 idx[i] += 1
#                 find_food(cal + food[i][1], score + food[i][0], count + 1,idx)
#                 idx[i] -= 1
#
# for tc in range(1,T+1) :
#
#     N, L = map(int,input().split())
#
#     food = [list(map(int,input().split())) for _ in range(N)]
#
#     max_v = 0
#
#     food_idx = [0]*N
#     find_food(0,0,0, food_idx)
#
#     print(f"#{tc} {max_v}")

T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    food = [list(map(int, input().split())) for _ in range(N)]

    # dp 배열 초기화
    dp = [[0] * (L+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(L+1):
            t, k = food[i-1]  # 현재 재료의 맛과 칼로리
            if j >= k:  # 현재 칼로리 제한을 넘지 않으면
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + t)
            else:
                dp[i][j] = dp[i-1][j]

    result = dp[N][L]
    print(f"#{tc} {result}")