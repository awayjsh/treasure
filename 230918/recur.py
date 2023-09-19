arr = [2,4,7,9,11,19,23]

arr.sort()

def binarySearch(low, high, target) :

    if low > high :

        return -1

    mid = (low + high) // 2

    if target == arr[mid] :

        return mid

    elif arr[mid] < target :

        return binarySearch(mid + 1, high, target)

    else :

        return binarySearch(low,mid - 1,target)

print(f'9 = {binarySearch(0,len(arr)-1,9)}')