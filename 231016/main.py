import math

R,C = map(int,input().split())

arr = [list(map(str,input())) for _ in range(R)]

direction = list(map(int,input()))

R_dircetion = []

dictionary = {
    1 : (1,-1),
    2 : (1,0),
    3 : (1,1),
    4 : (0,-1),
    5 : (0,0),
    6 : (0,1),
    7 : (-1,1),
    8 : (-1,0),
    9 : (-1,1)

}

for i in range(R) :

    for j in range(C) :

        if arr[i][j] == 'I' :

            start_i = i
            start_j = j

        if arr[i][j] == 'R' :

            R_dircetion.append((i,j))

print(R_dircetion)

while True :

    go_to = direction.pop(0)

    go_to = dictionary[go_to]

    arr[start_i][start_j] = '.'
    arr[start_i + go_to[0]][start_j + go_to[1]] = 'I'

    start_i = start_i + go_to[0]
    start_j = start_j + go_to[1]

    for idx in range(len(R_dircetion)):

        R_i, R_j = R_dircetion[idx]

        min_v = 1e9

        for i in range(1, 10):

            ni = R_i + dictionary[i][0]
            nj = R_j + dictionary[i][1]

            # Check if the new position is within the boundaries
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue

            # Check if the new position is not occupied by another 'R'
            if arr[ni][nj] == 'R':
                continue

            check = abs(start_i - ni) + abs(start_j - nj)

            if check < min_v:
                min_v = check
                new_i = ni
                new_j = nj

        arr[R_i][R_j] = '.'
        arr[new_i][new_j] = 'R'

        R_dircetion[idx] = (new_i, new_j)

    if len(direction) == 0 :

        break

print(R_dircetion)

for i in arr :

    print(i)