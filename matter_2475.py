# boj 2475번 문제 - 검증수 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.03   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n = list(map(int,input().split())) # 공백을 기준으로 숫자들을 받음
sum = 0 # 합계 = 0
for i in range(5): # 0 ~ 4까지 반복
    sum += (n[i] * n[i]) # n[i]을 제곱한 후 합계에 더함

print(sum % 10) # 합계의 일의 자리만 출력