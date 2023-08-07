voca = str(input())

def find_min(voca) :

    min = []
    count = 0

    for i in voca :

        if 'M' == i :

            count = count + 1

            if count == 1 :

                min.append("1")

            else :

                min.append("0")

        if 'K' == i :

            min.append("5")
            count = 0

    return "".join(min)

def find_max(voca) :

    max = []
    count = 0

    for i in voca :

        if "M" == i :

            count = count + 1

        if "K" == i :

            max.append("5")

            for j in range(count) :

                max.append("0")

            count = 0

    for i in range(count) :

        max.append("1")


    return "".join(max)

print(find_max(voca))
print(find_min(voca))