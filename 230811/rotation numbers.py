T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans1 = []
    ans2 = []
    ans3 = []
    part_ans = []

    for j in range(N):

        part_ans = []

        for i in reversed(range(N)):
            part_ans.append(arr[i][j])

        ans1.append(part_ans)

    for i in reversed(range(N)):

        part_ans = []

        for j in reversed(range(N)):
            part_ans.append(arr[i][j])

        ans2.append(part_ans)

    for i in reversed(range(N)):

        part_ans = []

        for j in reversed(range(N)):
            part_ans.append(arr[i][j])

        ans2.append(part_ans)

    for j in reversed(range(N)):

        part_ans = []

        for i in (range(N)):
            part_ans.append(arr[i][j])

        ans3.append(part_ans)

    print(f"#{tc}")

    for i in range(N):

        for j in range(N):

            if j == 0:

                for k in range(N):

                    if k != N - 1:
                        print(ans1[i][k], end="")
                    else:
                        print(ans1[i][k], "", end="")

            elif j == 1:

                for k in range(N):

                    if k != N - 1:
                        print(ans2[i][k], end="")
                    else:
                        print(ans2[i][k], "", end="")

            elif j == 2:

                for k in range(N):

                    if k != N - 1:
                        print(ans3[i][k], end="")
                    else:
                        print(ans3[i][k], "", end="")
                        print()