t = int(input()) # 테스트 케이스 개수

for tc in range(1, t+1):
    n, m = map(int,input().split()) #n*n배열, m*m파리채 크기
    arr = [list(map(int, input().split())) for _ in range(n)]

    #최대값
    max_fly = 0
    # (0,0) -> (n-m,n-m)까지 확인하기
    for i in range(n-m+1):
        for j in range(n-m+1):
            s = 0
            for c in range(i, i+m):
                for g in range(j, j+m):
                    s += arr[c][g]
            # 합의 최댓값 찾기
            if max_fly < s:
                max_fly = s

    print(f'#{tc} {max_fly}')