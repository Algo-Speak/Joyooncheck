T= int(input()) # T값을 정수로 입력 받는다

# 시간을 계산할 함수
def clock(H1,M1,H2,M2): # 매개변수 4개
    M = M1 + M2 # 분
    H = H1 + H2 + (M//60) # 시 , M이 60분이 넘어가면 추가로 받기
    if M >=60: # 분이 60을 넘어갈 때 예외 조건 설정(분 0 ~ 59분)
        M = M%60 # 60분의 나머지를 분으로 설정
    if H > 12 : # 12시는 12시로 표현
        H = H%12 # 시(1~12시)
    return H, M 

for tc in range(1, T+1):
    H1,M1,H2,M2 = map(int, input().split())
    H, M = clock(H1,M1,H2,M2)
    
    print(f'#{tc} {H} {M}')


