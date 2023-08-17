T = int(input())

def enq(data) :

    global rear
    global front

    if (front+1) % cQsize == front :

        front = (front + 1) % cQsize
    rear = (rear + 1) % cQsize
    cQ[rear] = data

def deq() :

    global front
    front = (front+1) % cQsize
    return cQ[front]

def isFull() :

    global front
    global rear
    return (rear+1) % len(cQ) == front

for tc in range(1,T+1) :

    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    idx = [i for i in range(1,M+1)]

    idx_arr = [[idx[i],arr[i]] for i in range(M)]

    cQsize = N
    cQ = [0] * cQsize

    front = 0
    rear = 0

    count = 0
    n = 0
    is_break = True
    ans = []

    while is_break :

        count = count + 1

        if count == 1 :

            enq(idx_arr.pop(0))

        else :

            n = cQ[(rear+1) % len(cQ)]

            if isinstance(n,int) and len(idx_arr) != 0:

                next_pizza = idx_arr.pop(0)
                enq(next_pizza)

            else :

                if n[1] // 2 == 0 and len(idx_arr) != 0:

                    deq()
                    next_pizza = idx_arr.pop(0)
                    enq(next_pizza)

                else :

                    cheese = n[1] // 2

                    enq([n[0],cheeze])


        ans_count = 0

        # print("cQ",cQ)
        # print("idx",idx_arr)

        if len(idx_arr) == 0 :

            for i in cQ :

                if i[1] == 0 :

                    ans_count += 1

                if ans_count == N-1 :

                    ans = cQ
                    is_break = False

    # print(ans)

    for i in ans :

        if i[1] != 0 :

            print(f"#{tc} {i[0]}")
            break




