# boj 10866번 문제 - 덱 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
from collections import deque # 덱큐를 사용하기 위함
import sys
input = sys.stdin.readline # 값을 빠르게 받기 위함

n = int(input()) # 받을 명령 갯수
d = deque()
for i in range(n):              # 0 ~ n까지 반복
    dq = input().split()        # dq에 값을 받음
    if dq[0] == "push_front":   # 덱 앞에 정수를 넣으라는 명령
        d.appendleft(dq[1])     # 덱 왼쪽에 정수를 넣음
    elif dq[0] == "push_back":  # 덱 뒤에 정수를 넣으라는 명령
        d.append(dq[1])         # 덱 오른쪽에 정수를 넣음
    elif dq[0] == "pop_front":  # 가장 앞에있는 정수를 빼어 출력하라는 명령
        if 0 == len(d):         # 덱이 비어있으면 -1 출력
            print(-1)
        else:                    # 비어있지않다면
            print(d.popleft())  # 명령 결과 출력
    elif dq[0] == "pop_back":   # 가장 뒤에있는 정수를 빼어 출력하라는 명령
        if 0 == len(d):     # 덱이 비어있다면 -1 출력
            print(-1)
        else:               # 비어있지않다면
            print(d.pop())  # 명령 결과 출력
    elif dq[0] == "size":   # 덱의 크기를 출력하라는 명령
        print(len(d))
    elif dq[0] == "empty":  # 덱이 비어있는지 확인하라는 명령
        if 0 == len(d):     # 비어있다면 1
            print(1)
        else:               # 비어있지않다면 0
            print(0)
    elif dq[0] == "front":  # 덱의 가장 앞에 있는 정수 출력
        if 0 == len(d):     # 없으면 -1
            print(-1)
        else:               # 있으면 첫번째 정수 출력
            print(d[0])
    else:                   # 덱의 가장 뒤에 있는 정수출력
        if 0 == len(d):     # 없으면 -1 출력
            print(-1)
        else:               # 있으면 마지막 정수 출력
            print(d[-1])