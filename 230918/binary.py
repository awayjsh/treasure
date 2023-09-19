arr = [2,4,7,9,11,19,23]

arr.sort()

def binarySearch(target) :

    low = 0
    high = len(arr) - 1

    while low <= high :

        mid = (low + high) // 2

        if arr[mid] == target :

            return mid

        elif arr[mid] < target :

            low = mid + 1

        else :

            high = mid - 1

    return "해당 데이터가 없습니다."

print(f'9 = {binarySearch(9)}')