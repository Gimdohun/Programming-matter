# boj 2164번 문제 - 카드 2 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
from collections import deque # 큐를 쓰기 위함
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
n = int(input()) # 카드의 개수를 입력받음
if n != 1: # n이 1이 아닐 경우
    s = [i for i in range(2,n + 1,2)] # 2의 배수로 이루어진 리스트를 생성(홀수는 첫단계에서 다 제거됨)
    s = deque(s) 
    if n % 2 == 0 and len(s) > 1: # 카드의 개수가 짝수개 였고 s 리스트의 길이가 1보다 크다면
        s.popleft() # 카드 하나뺌
    while len(s) != 1: # s 리스트가 1이 아닐때까지 반복(카드 한장남을때까지 반복)
        x = s.popleft() # s 리스트에서 카드 한장을 들고
        s.append(x)     # s 리스트의 맨뒤로 보냄
        s.popleft()     # s 카드 한장 제거
    print(s[0],end='') # 결과 출력
else: # 한장일 경우
    print(1,end='') # 1을 그대로 출력