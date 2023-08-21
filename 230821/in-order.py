def inorder(n) :

    if n:

        inorder(ch1[n])
        print(word[n-1],end = "")
        inorder(ch2[n])

for tc in range(1,11) :

    V = int(input())
    E = V-1

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    par = [0] * (V+1)
    word = []
    c = 0

    for i in range(V) :

        arr = list(map(str,input().split()))

        for i in range(len(arr)) :

            if i == 0 :

                p = int(arr[i])

            elif i == 1 :

                word.append(arr[i])

            else :

                c = int(arr[i])

                if ch1[p] == 0 :

                    ch1[p] = c

                else :

                    ch2[p] = c

            par[c] = p


    root = 1

    while par[root] != 0 :

        root += 1

    print(f"#{tc} ",end = "")

    inorder(root)

    print()