# boj 10773번 문제 - 제로#
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n = int(input()) # 받을 정수 개수
arr = []
for i in range(n): # 0 ~ n-1까지 반복 (n번 반복)
    x = int(input()) # x에 정수를 받음
    if x == 0: # 0일 경우
        if len(arr) != 0: # arr의 길이가 0이 아닐경우(삭제할 원소가 있을 경우
            arr.pop() # arr에서 원소 하나 삭제
    else: # 0이 아닐경우
        arr.append(x) # 사용자 입력값 추가

print(sum(arr)) # 사용자 입력값에서 합계 출력