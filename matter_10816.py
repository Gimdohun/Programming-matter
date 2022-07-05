# boj 10816번 문제 - 숫자카드 2#
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
n = int(input()) # 가지고 있는 숫자카드 개수 입력
arr = list(map(int,input().split())) # 가지고 있는 숫자카드 리스트 입력
m = int(input()) # 찾을 숫자카드 개수입력
find = list(map(int,input().split())) # 찾을 숫자카드 리스트 입력
hashing = {} # 해시 테이블

for i in arr: # arr 원소를 i에 담음
    if i in hashing: # 해시 테이블에 i가 있는경우
        hashing[i] += 1 # 해시테이블의 i값에 1을 더함
    else: # 해시 테이블에 i가 없는 경우
        hashing[i] = 1 # 해시 테이블 i번 추가

for i in find: # 찾으려는 원소를 i에 하나씩 대입 입력
    if i in hashing: # 해시 테이블에 i가 있는 경우
        print(hashing[i],end=' ') # 해시 테이블 i번 출력
    else: # 없는 경우
        print(0,end=' ') # 0 출력