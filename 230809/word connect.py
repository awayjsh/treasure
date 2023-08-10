N = int(input())
words = []

if N == 1:
    word = input()
    M = int(input())
    ans = input()

else:
    for i in range(N):
        word = input()
        words.append(word)

M = int(input())

if words[0] == '?':
    end_s = words[1][0]
    for i in range(M):
        str = input()
        if str[0] == end_s and str not in words:
            ans = str
            break
elif words[-1] == '?':
    start_s = words[-2][-1]
    for i in range(M):
        str = input()
        if str[-1] == start_s and str not in words:
            ans = str
            break
else:
    ans_idx = words.index('?')
    end_s = words[ans_idx-1][-1]
    start_s = words[ans_idx+1][0]
    for j in range(M):
        str = input()
        if str[0] == end_s and str[-1] == start_s and str not in words:
            ans = str
            break
print(ans)