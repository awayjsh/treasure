# T = int(input())
#
# for tc in range(1, T +1):
#     N = float(input())
#     ans = ''
#
#     i = 0
#
#     zari = 1.0  # 초기 자리수
#
#     while i<12 and N != 0.0:
#         hh = 2 ** ((-1) * zari)
#         if hh <= N:
#             ans += '1'
#             N -= hh
#         else:
#             ans += '0'
#         zari += 1
#         i += 1
#         if zari > 12:  # 13자리 이상일 때
#             ans = 'overflow'
#             break
#
#     print(f'#{tc} {ans}')

new_list = ['ALAKIR', 'LORD-JARAXXUS', 'ALEXSTRASZA', 'AVIANA', 'DR-BOOM']

print(*new_list)