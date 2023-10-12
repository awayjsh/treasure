import copy

arr = [list(map(int, input().split())) for _ in range(4)]
new = [[] for _ in range(4)]
visited = [[0] * 4 for _ in range(4)]

dic = {
    1 : (-1,0),
    2 : (-1,-1),
    3 : (0,-1),
    4 : (-1,1),
    5 : (1,0),
    6 : (1,1),
    7 : (0,1),
    8 : (1,-1),
}

for i in range(4) :

    for j in range(0,7,2) :

        new[i].append([arr[i][j],dic[arr[i][j+1]]])

for i in range(4) :

    for j in range(4) :

        new[i][j].append((i,j))






