# boj 2475번 문제 - 음계 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.03   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
a = 9 # descending인지 검사하기 위해 저장한 수 + 1
arr = list(map(int,input().split())) # 배열에 사용자 값을 담음
for i in range(8): # 0 ~ 7까지 반복
    if arr[i] == i + 1: # 첫번째 배열부터 i + 1(1 ~ 8)이라는 숫자로 고르게 정렬되어있는지 확인
        s = "ascending" # 맞다면 ascending
    else: # 아니라면
        for i in range(8): # 0 ~ 7까지 반복
            a -= 1 # a에서 1을 뺌(8부터 확인하며 내려가야되는데, 반복문의 첫단부터 등장하기때문에 처음에 수를 8이 아닌 9로 줌)
            if arr[i] == a: # 첫번째 배열부터 8부터 시작한 내림차순으로 정렬되어있는지 확인
                s = "descending" # 맞다면 descending
            else: # 하나라도 틀리다면
                s = "mixed" # mixed
                break # 반복문 종료
        break # 반복문 종료

print(s,end='') # s 결과 출력