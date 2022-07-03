# boj 24463번 문제 - 요세푸스 문제 0 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.03   #
from collections import deque # 큐를 쓰기 위함
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n, k = map(int,input().split()) # 총 인원수와 제거될 위치 입력
a = [i for i in range(1,n + 1)] # 1 ~ n까지의 수를 a에 담음
a = deque(a) # a를 큐에 저장
s = [] # 제거된 사람 저장
c = 0 # 탐색할 때마다 카운터
while len(s) < n: # 모두 제거될 때까지 반복
    c += 1 # c + 1번째 확인
    if c == k: # 제거될 위치와 확인한 횟수가 같다면
        x = a.popleft() # a에서 제거
        s.append(x) # 제거 목록에 저장
        c = 0 # 처음부터 다시 확인
    else: # 제거될 위치가 아니라면
        x = a.popleft() # x에 저장후
        a.append(x) # 맨뒤로 보냄
print("<",end='') # '<' 출력
for i in range(len(s)): # 0 ~ s의 길이 - 1만큼 반복
    if i == len(s) - 1: # 마지막이라면
        print("%d>"%s[i]) # "마지막 번호와 '>' 출력
    else: # 마지막이 아니라면
        print(s[i],end=', ') # 번호출력 후 ', ' 출력

