# boj 1806번 문제 - 부분합 #
#     작성자 : 김도훈    #
#   날짜 : 2022.06.29   #

import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n,s = map(int,input().split()) # n = 받는 수의 개수, s = 확인해야될 값중 최소 값
array = [] # 배열

array = list(map(int,input().split())) # 배열에 값을 넣음
start = 1 # 시작 인덱스
end = 1 # 종료 인덱스
min_index = s # 최소 인덱스 개수(모든 인덱스를 가지는 걸로 초기화)
sum_value = 0 # 합계값
prefix_sum = [0] # 부분합
possible = 0 # s 이상의 값이 나오는 지 여부
for i in array: # array 배열을 부분합으로 바꿈
    sum_value += i
    prefix_sum.append(sum_value)

while end <= n and start <= n: # end 그리고 start가 array 인덱스를 안넘는다면 반복
    if prefix_sum[end] - prefix_sum[start - 1] < s: # 부분합 = P[R] - P[L-1] = 구하려는 마지막 인덱스 값 - 시작 인덱스값 - 1
        # s보다 작다면 end값 1증가
        end += 1
    else: # s보다 크고 최소 인덱스 개수보다 start에서 end까지의 인덱스 길이가 더 작다면 최소 인덱스 개수 저장 변수에 인덱스 길이 대입
        if min_index > end - (start-1):
            min_index = end - (start-1)
        start += 1 # 크거나 같다면 start값 1증가
        possible = 1 # s이상 나오는 게 가능한 일이니 possible 1추가

if possible == 0: # 가능하지 않다면
    min_index = 0 # 최소 인덱스에 0 대입
print(min_index) # 최소 인덱스 출력