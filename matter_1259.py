# boj 1259번 문제 - 팰린드롬수 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.03   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함
n = list(input()) # 수를 받음
s = [] # 팰린드롬수인지 여부 확인
yorn = 1 # yes = 1 no = 0
while True: # 무한 반복문
    l = len(n) - 1 # n의 배열 길이에서 개행문자 제외하여 l에 담음
    if n[0] == '0': # 처음에 0을 입력할 경우 종료
        break
    j = l // 2 # n의 배열의 반만 확인(앞과 뒤를 대조)
    l -= 1 # n의 마지막 인덱스
    for i in range(j): # 0 ~ j - 1까지 반복
        if n[l] != n[i]: # 뒷부분과 앞부분이 같지않다면
            yorn = 0 # 같지않음 표시
            break # 확인 종료(한 곳이라도 다르면 더 확인해볼 필요 X)
        l -= 1 # 같다면 다음 인덱스 비교
    if yorn == 1: # 반복문을 통과했다면
        s.append('yes') # s에 'yes'를 담음
    else: # 같지않아 반복문을 강제종료했다면
        s.append('no') # s에 'no'를 담음
        yorn = 1 # 같음 표시
    n = list(input()) # 사용자가 입력하는 숫자를 리스트로 받음

l = len(s) # s의 배열 길이를 l에 입력받음
for i in range(l): # 0 ~ l - 1까지 반복
    print(s[i]) # s[i]번 요소('yes' 또는 'no')를 출력 후 개행
