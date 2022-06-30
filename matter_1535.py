# boj 1535번 문제 - 안녕 #
#     작성자 : 김도훈    #
#   날짜 : 2022.06.30   #
import sys
input = sys.stdin.readline # 입력을 빨리 받기 위함

n = int(input()) # 만나는 사람 수
feel = [[0,0]] # 기분 저장 배열
i = list(map(int,input().split())) # 인사할때 잃는 체력
j = list(map(int,input().split())) # 인사할 경우 얻는 기쁨
dp = [[0] * (100) for i in range(n+1)] # 체력이 100에서 0이되면 죽으므로 99까지 체력 소비할 수 있는 dp테이블
for k in range(0,n): # 기분 저장 배열에 인사할 때 잃는 체력과 얻는 기쁨을 넣음
    feel.append([i[k],j[k]])

for i in range(1, n + 1): # 1 ~ n 까지 반복
    for j in range(1, 100): # 1 ~ 99까지 반복
        if j >= feel[i][0]: # 가진 체력이 인사할경우 잃는 체력보다 많다면
            # 인사했을 경우 + 남은 체력으로 다른사람과도 인사했을 경우와 인사를 안했을 경우 중 더 큰 기쁨을 주는 것을 dp에 넣음
            dp[i][j] = max(dp[i-1][j],dp[i-1][j - feel[i][0]] + feel[i][1])
        else: # 남는 체력이 더 없을 경우
            # dp는 인사 안했을 경우와 동일
            dp[i][j] = dp[i-1][j]

# 99 체력으로 최대한의 기쁨을 얻었을 경우를 출력
print(dp[n][99])