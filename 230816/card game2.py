T = int(input())

def divided(a,b) :

    if a == b :

        return a

    else :

        new_a = divided(a,(a+b)//2)
        new_b = divided((a+b)//2 + 1, b)

        return game(new_a, new_b)

def game(a,b) :

    if (arr[a] == 1 and arr[b] == 3) or (arr[a] == 2 and arr[b] == 1) or (arr[a] == 3 and arr[b] == 2) :

        return a

    elif (arr[a] == 3 and arr[b] == 1) or (arr[a] == 1 and arr[b] == 2) or (arr[a] == 2 and arr[b] == 3) :

        return b

    elif (arr[a] == 3 and arr[b] == 3) or (arr[a] == 1 and arr[b] == 1) or (arr[a] == 2 and arr[b]== 2) :

        return a


for tc in range(1,T+1) :

    N = int(input())

    arr = list(map(int,input().split()))

    print(f"#{tc} {divided(0,N-1)+1}")