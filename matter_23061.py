# boj 14728번 문제 - 백남이의 여행준비 #
#     작성자 : 김도훈    #
#   날짜 : 2022.06.30   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
n,m = map(int,input().split()) # 물품의 수와 가방의 수 입력
item = [[0,0]] # 넣을 물건의 무게와 가치
bag = [] # 가방의 종류
for i in range(n): # n번 반복
    w,v = map(int,input().split()) # 무게와 가치를 받음
    item.append([w,v]) # 받은 데이터를 배열에 넣음
max_value = 0 # 최대 무게 = 0
for i in range(m): # m번 반복
    a = int(input()) # 가방의 최대 무게
    bag.append(a) # 가방의 종류 배열에 넣음
    if max_value < a: # 최대 무게가 a보다 작을 시
        max_value = a # 최대 무게 갱신

# 최대무게 + 1 만큼의 dp 2차원 테이블 생성
dp = [[0] * (max_value + 1) for i in range(n + 1)]

for i in range(1,n + 1): # 1 ~ n까지
    for j in range(1, max_value + 1): # 1 ~ 최대무게까지
        if j >= item[i][0]: # 넣을 수 있는 무게가 물건의 무게보다 크거나 같을경우
            # 물건을 안넣었을 경우와 물건을 넣었을 경우 + 남은 공간에 다른 걸 넣었을 경우 중 큰 값을 대입
            dp[i][j] = max(dp[i-1][j],dp[i-1][j - item[i][0]] + item[i][1])
        else: # 작은경우
            dp[i][j] = dp[i-1][j] # 안넣었을 때의 최대가치 대입


c = 0 # 가치있는 가방의 번호
max_efficiency = -1 # 물건을 넣음으로 부터의 가치
efficiency_bag = 0 # 효율적인 가방 인덱스 번호
for i in bag: # 가방의 정보 입력
    c += 1 # 다음 가방 번호
    # 현재 가방의 효율성(최대 가치 / 가방의 무게)이 현재까지 나온 가장 효율적인 가방보다 클 경우
    if dp[n][i] / i > max_efficiency: 
        # 최대 효율성 갱신
        max_efficiency = dp[n][i] / i
        # 가장 좋은 가방 번호 갱신
        efficiency_bag = c

# 가장 효율 좋은 가방 번호 출력
print(efficiency_bag)

