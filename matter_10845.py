# boj 10845번 문제 - 큐 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
from collections import deque # 덱큐를 사용하기 위함
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n = int(input()) # 명령의 개수를 입력 받음
q = deque()
for i in range(n): # 0 ~ n-1까지(n번) 반복
    queue = input().split() # 명령을 받음
    if queue[0] == "push": # 명령이 push인 경우
        q.append(queue[1]) # 명령 뒤에 따라오는 정수를 큐에 넣음
    elif queue[0] == "pop": # 명령이 pop인 경우
        if 0 == len(q): # 큐의 길이가 0인 경우(큐에 아무것도 없는 경우)
            print(-1) # -1 출력
        else: # 아닌경우
            print(q.popleft()) # 큐의 왼쪽 원소를 뽑은 후 출력
    elif queue[0] == "size": # 명령이 size인 경우
        print(len(q)) # 큐의 길이 출력
    elif queue[0] == "empty": # 명령이 empty인 경우
        if 0 == len(q): # 큐의 길이가 0인 경우(큐에 아무것도 없는 경우)
            print(1) # 1을 출력
        else: # 아닌경우
            print(0) # 0을 출력
    elif queue[0] == "front": # 명령이 empty인 경우
        if 0 == len(q): # 큐의 길이가 0인 경우(큐에 아무것도 없는 경우)
            print(-1) # -1을 출력
        else: # 아닌경우
            print(q[0]) # 큐의 첫번째 원소 출력
    else: # 명령이 back인 경우(위의 명령중 일치하는 명령이 없는경우)
        if 0 == len(q): # 큐의 길이가 0이라면
            print(-1) # -1 출력
        else: # 아닌경우
            print(q[-1]) # 큐의 마지막 원소 출력