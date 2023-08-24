T = int(input())

for tc in range(1,T+1) :

    arr = list(map(str, input()))
    j = 1 # 비교당하는 문자 인덱스!

    while True :

        if arr[0] == arr[j] and arr[1] == arr[j+1] : # 만약 비교당하는 문자도 같고 그 뒤에 문자도 같다면

            break # 멈춰!

        j += 1 # 아니면 j 증가해서 계속 반복해...

    print(f"#{tc} {j}") # 그렇다면 j의 위치가 다시 반복되는 문자의 시작일테니까 j만 출력하면 길이를 알 수 있음!