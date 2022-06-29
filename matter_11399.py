# boj 11399번 문제 - ATM #
#     작성자 : 김도훈    #
#   날짜 : 2022.06.29   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
n = int(input()) # 사람 수
array = list(map(int,input().split())) # 사람들의 걸리는 시간 저장
time = 0 # 기다려야되는 시간 + 자신이 사용하는 시간
s = 0 # 모든 사람들이 기다린 시간 + 모든 사람들이 사용한 시간
array.sort() # 정렬(시간이 적게 걸리는 사람이 먼저해야 모든 사람들이 소비한 시간의 합이 적게나옴)
for i in array: # 사람들이 걸리는 시간을 한명씩 i에 대입
    time += i # 한명이 기다리고 사용하는 시간
    s += time # 총합

print(s) # 총합 출력