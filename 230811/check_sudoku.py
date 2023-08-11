T = int(input())

def sudoku(arr) :

    for i in range(9):

        cnt1 = [0] * 10

        for j in range(9):

            cnt1[arr[i][j]] += 1

        for k in range(1, 10):

            if cnt1[k] == 0:
                return 0

    for j in range(9) :

        cnt2 = [0] * 10

        for i in range(9) :

            cnt2[arr[i][j]] += 1

        for k in range(1,10) :

            if cnt2[k] == 0 :
                return 0

    for i in range(0,7,3) :

        for j in range(0,7,3) :

            cnt3 = [0] * 10

            for k in range(i,i+3) :

                for l in range(j, j+3) :

                    cnt3[arr[k][l]] += 1

            for a in range(1,10) :

                if cnt3[a] == 0 :

                    return 0

    return 1

for tc in range(1,T+1) :

    arr = [list(map(int, input().split())) for _ in range(9)]

    print(f"#{tc} {sudoku(arr)}")



