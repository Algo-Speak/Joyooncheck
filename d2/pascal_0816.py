# T 테스트케이스
# N 삼각형의 크기
# arr 배열칸

T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    arr = [[0]*(N+1) for _ in range(N+1)] # 숫자를 담을 배열판
    arr[1][1] = 1 # 이제 배열판에 숫자 채워주기
    for i in range(2, N+1): # arr[1][1]에는 이미 1이 있으니 2부터 시작
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j] #자신의 왼쪽과 오른쪽 위의 숫자의 합
    print(f'#{tc}')
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(arr[i][j], end = ' ')
        print()