x = int(input())
ans = 1e9

def makeone(count,num) :

    global ans

    if count >= ans :

        return

    if num == 1 :

        ans = min(ans,count)
        return

    else :

        if num % 3 == 0 :

            makeone(count+1,num//3)

        if num % 2 == 0 :

            makeone(count+1,num//2)

        makeone(count+1,num - 1)

makeone(0,x)

print(ans)