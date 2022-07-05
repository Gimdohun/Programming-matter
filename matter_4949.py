# boj 4949번 문제 - 균형잡힌 세상 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
from collections import deque # 덱큐를 사용하기 위함
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
s = []
pm = []
while True: # 무한 반복문
    s = input() # 문장을 받음
    if len(s) == 2 and s[0] == '.': # 사용자가 '.'만 입력했다면 종료
        break
    t = deque()
    for i in range(len(s) - 1): # 0 ~ s의 마지막 배열 번호까지(len(s) - 1인 이유는 개행문자를 무시하기 위함) 반복
        if s[i] == '(': # 여는 소괄호를 발견할 경우
            t.append('(') # 덱큐에 넣음
        elif s[i] == '[': # 여는 대괄호를 발견할 경우
            t.append('[') # 덱큐에 넣음
        elif s[i] == ')': # 닫는 소괄호를 발견할경우
            if len(t) == 0 or '(' != t.pop(): # 덱큐에 아무것도 없거나 덱큐의 끝 요소를 추출하였는데 닫는 소괄호가 아닌경우
                pm.append("no") # no를 리스트에 추가하고(균형X) 반복문 종료
                break
        elif s[i] == ']': # 닫는 대괄호를 발견한 경우
            if len(t) == 0 or '[' != t.pop(): # 덱큐에 아무것도 없거나 덱큐의 끝 요소를 추출하였는데 닫는 대괄호가 아닌경우
                pm.append("no") # no를 리스트에 추가하고(균형X) 반복문 종료
                break
        if i == len(s)-2: # 아무문제 없이 개행문자를 제외한 s의 마지막 배열까지 다확인했다면
            if len(t) == 0: # 덱큐에 남아있는 괄호가 없다면
                pm.append("yes") # yes를 리스트에 추가
            else: # 아닌경우
                pm.append("no") # no를 리스트에 추가


for i in pm: # 추가된 리스트 출력(yes or no)
    print(i)