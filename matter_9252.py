# boj 9252번 문제 - LCS2 #
#     작성자 : 김도훈    #
#   날짜 : 2022.06.30   #
import sys
input = sys.stdin.readline
# 입력을 빠르게 받기 위함
a = str(input()) # 첫번째 문장을 받음
b = str(input()) # 두번째 문장을 받음
alen = len(a) - 1 # a의 길이 - 1
blen = len(b) - 1 # b의 길이 - 1
# 2차원 dp테이블 생성
dp = [['0'] * (alen + 1) for _ in range(blen + 1)]

for i in range(1, blen + 1): # 1 ~ b의 길이까지
    for j in range(1, alen + 1): # 1 ~ a의 길이까지
        if a[j - 1] == b[i - 1]: # a의 j - 1번째 원소와 b의 i - 1번째 원소가 같다면
            dp[i][j] = dp[i-1][j-1] + a[j - 1] # a의 j - 1원소와 b의 i - 1 원소가 없을 때의 경우 + 1
        else: # 다를경우
            # i - 1원소가 없을때의 길이와 j - 1원소가 없을 떄의 길이 중 더 큰 값 대입
            if len(dp[i-1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[blen][alen]) - 1) # dp의 문자열 길이 출력(초기의 '0'은 제외)
if len(dp[blen][alen]) > 1: # dp가 0이 아닐 때
    print(dp[blen][alen][1:])  # dp의 문자열 출력(초기의 '0'은 제외)
