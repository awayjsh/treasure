N = int(input())

white = [[0] * 100 for _ in range(100)]

count = 0

for i in range(N) :

    a, b = map(int,input().split())

    for i in range(10) :

        for j in range(10) :

            white[a + i][b + j] = 1

for i in range(100) :

    for j in range(100) :

        if white[i][j] == 1 :

            count = count + 1

print(count)