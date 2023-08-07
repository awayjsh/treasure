T = int(input())

for tc in range(1,T+1) :

    test_num, N = map(str, input().split())

    N = int(N)

    arr = list(map(str, input().split()))

    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_count = [0] * 10

    for i in range(N) :

        for j in range(10) :

            if arr[i] == num_list[j] :

                num_count[j] = num_count[j] + 1

    print(f"{test_num}")

    for i in range(10) :

        for j in range(num_count[i]) :

            print(num_list[i], end = " ")
    print()