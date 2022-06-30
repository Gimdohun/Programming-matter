# boj 1958번 문제 - LCS3 #
#     작성자 : 김도훈    #
#   날짜 : 2022.06.30   #
import sys
# 입력을 빠르게 받기 위함
input = sys.stdin.readline

a = str(input()) # 첫번째 문장을 받음
b = str(input()) # 두번째 문장을 받음
c = str(input()) # 세번째 문장을 받음
alen = len(a) # 첫번째 문장의 문자열 길이
blen = len(b) # 두번째 문장의 문자열 길이
clen = len(c) # 세번째 문장의 문자열 길이
# dp를 3차원 배열로 초기화
dp = [[[0] * (alen) for _ in range(blen)] for _ in range(clen)]

for i in range(1,clen): # 1 ~ 세번쨰 문자열 - 1까지
    for j in range(1,blen): # 1 ~ 두번쨰 문자열 - 1까지
        for k in range(1,alen): # 1 ~ 첫번째 문자열 - 1까지
            if a[k - 1] == b[j - 1] == c[i - 1]: # a의 k - 1번째 원소, b의 j - 1번째 원소, c의 i - 1번째 원소가 모두 같을경우 
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1 # dp테이블은 abc 세 원소가 존재하지 않았을 경우에 + 1
            else: # 다른 경우
                # i가 존재하지않은 경우, j가 존재하지않은 경우 k가 존재하지않은 경우 중 가장 큰거 대입
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

# 최종값 출력
print(dp[clen - 1][blen - 1][alen - 1])