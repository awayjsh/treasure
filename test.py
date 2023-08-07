def atoi(s) :

    i = 0

    for x in s :

        i = i * 10 + ord(x) - ord('0')

    return i

def itoa(a) :

    s = ''

    while a > 0 :

        s += chr(ord('0') + a % 10) # 1의 자리 숫자의 아스키 값을 알아내는 과정
        a //= 10

    return s[::-1]

