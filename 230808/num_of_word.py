T = int(input())

for tc in range(1,T+1) :

    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    len_str1 = 0

    for i in str1 :

        len_str1 = len_str1 + 1

    num_count = [0] * len_str1

    for j in str2 :

         for i in range(len_str1):

            if str1[i] == j :

                num_count[i] = num_count[i] + 1

    max = 0

    for i in num_count :

        if i >= max :

            max = i

    print(f"#{tc} {max}")
