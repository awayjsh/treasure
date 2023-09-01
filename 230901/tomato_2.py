
from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
q = deque()
# visited = [[False]*M for _ in range(N)]
cnt_lst = [[-1]*M for _ in range(N)]
flag = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))
            cnt_lst[i][j] = 0
        # elif tomato[i][j] == -1:
        #     cnt_lst[i][j] = 0
        elif tomato[i][j] == 0:
            flag += 1

# print(cnt_lst)
# print(q)

while q:
    x, y = q.popleft()
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx, ny = x+dx, y+dy

        if 0<=nx<N and 0<=ny<M and cnt_lst[nx][ny] == -1 and tomato[nx][ny] == 0:
            cnt_lst[nx][ny] = cnt_lst[x][y] + 1
            q.append((nx, ny))
        elif 0<=nx<N and 0<=ny<M and cnt_lst[nx][ny] == -1 and tomato[nx][ny] == -1:
            continue

print(cnt_lst)


ans = 0
for cnt in cnt_lst:
    if -1 in cnt:
        ans = -1
        break
    else:
        if max(cnt) > ans:
            ans = max(cnt)

if flag == 0:
    ans = 0

print(ans)