T = int(input())

for tc in range(1, T+1) :

    A, B = map(str, input().split())
    start_idx = 0
    count = 0

    for i in range(len(A)) :

        part_A = A[start_idx : start_idx + len(B)]
        if part_A == B :

            count = count + 1
            start_idx = start_idx + len(B)

        else :

            start_idx = start_idx + 1

    remain = len(A)

    for i in range(count) :

        remain = remain - len(B)

    print(f"#{tc} {remain + count}")
