# boj 1966번 문제 - 프린터 큐 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
from collections import deque # 덱큐를 쓰기 위함
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
t = int(input())  # 테스트 케이스를 받음
for i in range(t): # 0~t-1까지 반복
    arr = deque()
    m, index = map(int,input().split()) # 출력해야되는 출력물의 개수, 순서를 확인할 인쇄물 위치
    s = list(map(int,input().split())) # 출력 예정 리스트를 받음
    for i in range(m): # 0 ~ m-1까지 반복
        arr.append((s[i],i)) # 큐에 리스트의 원소와 현재 출력 순위를 넣음
    i = 0
    c = 0
    while True: # 무한 반복문
        if arr[0][0] == max(arr)[0]: # 현재 0번째 출력물이 출력물 우선순위 중 가장 높은 경우
            t1,t2 = arr.popleft() # 큐에서 원소를 꺼내서 t1,t2에 담음 t1 = 출력물 중요도,t2 = 초기의 출력 순위(인덱스번호)
            if t2 == index: # 인덱스 번호가 사용자가 출력의 순위를 알고 싶었던 출력물의 인덱스 번호와 일치하는 경우
                print(c+1) # 순서 출력 후 종료
                break
            c += 1
        else:  # 아닐경우
            arr.append(arr.popleft()) # 큐의 맨뒤로 보냄