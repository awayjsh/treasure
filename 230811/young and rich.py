# T = int(input())
#
# for tc in range(1, T+1) :
#
#     N = int(input())
#     arr = list(map(int, input().split()))
#     ans = 0
#
#     for i in range(N) :
#
#         total = 0
#
#         for j in range(i+1,N) :
#
#             if arr[j] - arr[i] <= 0 :
#
#                 continue
#
#             else :
#
#                 if total <= (arr[j] - arr[i]) :
#
#                     total = arr[j] - arr[i]
#
#         ans = ans + total
#
#     print(f"#{tc} {ans}")