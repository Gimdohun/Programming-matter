# boj 12865번 문제 - 평범한 배낭 #
#        작성자 : 김도훈        #
#      날짜 : 2022.06.29       #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
n,k = map(int,input().split()) # n = 물건의 개수, k = 최대들 수 있는 무게
dp = [[0] * (k + 1) for _ in range(n + 1)] # dp테이블을 0으로 초기화
item = [[0,0]] # 물건 정보 저장

for i in range(n): # 물건 정보를 리스트에 추가
    item.append(list(map(int,input().split())))

for i in range(1, n + 1): # 1 ~ n(물건의 수)까지 반복
    for j in range(1, k + 1): # 1 ~ k(최대 무게)까지 반복
        if j >= item[i][0]: # 만약 물건의 무게가 j의 최대 무게보다 작다면
            # i의 물건이 있다고 가정, j의 무게까지가 마지노선일때의 경우에서  아래 두 경우 중 가장 큰 가치를 담을 수 있는 값 대입
            # 1. i 물건이 없을때 j의 무게가 마지노선일 경우
            # 2. i 물건을 가져갔을 때의 가치 + 남은 무게 중 최대의 가치를 가진 경우
            dp[i][j] = max(dp[i-1][j],dp[i-1][j - item[i][0]] + item[i][1])
        else: # 가져갈 수 있는 무게가 더 작아서 i를 가져갈 수 없을 경우
            # i 물건이 있다고 가정 하더라도, 가져가지는 못하니 없을 때 최대의 가치를 대입
            dp[i][j] = dp[i-1][j]

print(dp[n][k]) # 결론적으로 나온 최대의 가치 출력