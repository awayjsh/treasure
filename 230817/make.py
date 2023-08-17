for i in range(1,11) :

    tc = int(input())

    arr = list(map(int, input().split()))

    is_break = 0

    while not is_break:

        num = [1,2,3,4,5]

        for i in range(5) :

            n = arr.pop(0)

            n = n - num[i]

            if n <= 0 :

                n = 0
                is_break = 1

            arr.append(n)

            if is_break:

                break

    print(f"#{tc}",*arr)