# boj 10816번 문제 - 스택#
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n = int(input()) # 명령 개수 입력
s = []
for i in range(n): # 0 ~ n-1까지 반복(n번 반복)
    stack = input().split()
    if stack[0] == "push": # 명령이 push인 경우
        s.append(stack[1]) # stack 뒤에 온 정수를 리스트에 넣음
    elif stack[0] == "pop": # 명령이 pop인 경우
        if 0 == len(s): # 스택 길이가 0이면
            print(-1) # -1 출력
        else: # 0이아닌경우
            print(s.pop()) # pop명령 실행 후 출력
    elif stack[0] == "size": # 명령이 size인 경우
        print(len(s)) # 스택의 길이 출력
    elif stack[0] == "empty": # 명령이 empty인 경우
        if 0 == len(s): # 길이가 0일경우(비어있다면)
            print(1) # 1출력
        else: # 아닐경우
            print(0) # 0 출력
    else: # 명령이 top인 경우(위의 모든 명령과 일치하지 않을경우)
        if 0 == len(s): # 길이가 0이라면
            print(-1) # -1 출력
        else: # 길이가 0이 아니라면
            print(s[-1]) # 제일 위에있는 원소 출력
