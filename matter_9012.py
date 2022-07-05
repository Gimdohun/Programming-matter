# boj 9012번 문제 - 괄호 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n = int(input()) # 문자열의 개수를 입력받음
result = []
for i in range(n): # 0~n-1까지 n번 반복
    s = input() # 문자열을 입력 받음
    vps = 0
    for j in range(len(s) - 1): # 0 ~ 문자열 마지막 배열(개행문자 제외)까지 반복
        if s[j] == ')': # 닫는 괄호면
            vps -= 1 # vps에서 1을 빼줌
        elif s[j] == '(': # 여는 괄호면
            vps += 1 # vps에서 1을 더해줌
        if vps < 0: # vps가 음수가 되었음 = 닫는 괄호가 여는 괄호가 나오기 전에 먼저 나왔거나 더 많이 나옴
            break # 종료
    if vps == 0: # vps가 0이라면 -> 여는 괄호와 닫는괄호의 개수가 같은 경우
        result.append("YES") # 결과 리스트에 Yes 추가
    else: # 아닐경우
        result.append("NO") # 결과 리스트에 NO 추가

for i in result: # 결과 리스트 값을 i에 하나씩 대입
    print(i) # 결과출력