# boj 14728번 문제 - 벼락치기 #
#     작성자 : 김도훈    #
#   날짜 : 2022.06.30   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
n,t = map(int,input().split()) # 시험치는 과목의 갯수와 보유 시간
exam = [[0,0]] # 예상공부시간, 배점
# dp 2차원 테이블 생성
dp = [[0] * (t + 1) for _ in range(n + 1)]
for i in range(n): # n번 반복
    k,s = map(int,input().split()) # 시간과 점수를 입력
    exam.append([k,s]) # 시험 배열에 넣음

for i in range(1,n + 1): # 1 ~ n까지 반복
    for j in range(1, t + 1): # 1 ~ t까지 반복
        if j >= exam[i][0]: # 남은 시간이 시험공부 소요시간보다 많을 경우
            # 해당 과목을 공부안했을 때와 해당 과목을 하고 남은 시간 다른 공부를 했을때의 배점 비교
            dp[i][j] = max(dp[i-1][j],dp[i-1][j - exam[i][0]] + exam[i][1])
        else: # 적을 경우
            # 해당 과목을 패스하고 받는 점수를 넣음
            dp[i][j] = dp[i-1][j]

# 최종 값 출력
print(dp[n][t])

