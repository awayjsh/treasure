N = int(input())

switch = list(map(int,input().split()))

people = int(input())

for i in range(people) :

    a,b = map(int,input().split())

    if a == 1 :

        for i in range(b-1,N,b) :

            if switch[i] == 0 :

                switch[i] = 1

            elif switch[i] == 1 :

                switch[i] = 0

    elif a == 2 :

        l = 0

        b = b - 1

        while True :

            if b + l >= N or b - l < 0 :

                break

            if switch[b + l] == switch[b-l] and b+l != b-l :

                if switch[b+l] == 0 :

                    switch[b+l] = 1

                elif switch[b+l] == 1 :

                    switch[b+l] = 0

                if switch[b-l] == 0 :

                    switch[b-l] = 1

                elif switch[b-l] == 1 :

                    switch[b-l] = 0

            elif switch[b + l] == switch[b-l] and b+l == b-l :

                if switch[b] == 0:

                    switch[b] = 1

                elif switch[b] == 1:

                    switch[b] = 0

            elif switch[b + l] != switch[b-l] :

                break

            l = l + 1

count = 0

for i in range(0,N) :

    print(switch[i], end = " ")

    count = count + 1

    if count == 20 :

        print()
        count = 0