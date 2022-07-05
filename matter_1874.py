# boj 1874번 문제 - 스택 수열 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
from collections import deque            # 덱큐를 사용하기 위함
import sys
input = sys.stdin.readline               # 입력을 빠르게 받기 위함

n = int(input())                         # 수열의 길이를 입력받음
s = []
num = [i for i in range(1,n + 1)]        # 1~n까지의 원소를 담은 리스트를 선언
num = deque(num)
t = []
pm = []
for i in range(n):                       # 사용자가 입력하는 수열을 s에 저장
    x = int(input())
    s.append(x)
i = 0
while i < n:                             # i가 n과 같거나 크면 종료(i 초기값이 0이니까 n번 반복)
    # 1~n까지 담겨있는 큐에 모든 원소를 빼지 않은 경우와 큐에 첫번째 원소가 i번째 요소와 작거나 같을 경우
    # (1씩 증가하는 수열의 첫번째 원소가 사용자가 만든 수열보다 크다는 말은 사용자가 원하는 수가 큐에 없다는 걸 뜻함)
    if len(num) != 0 and num[0] <= s[i]:
            while num[0] < s[i]:         # 사용자가 원하는 수열의 원소가 나올때까지 반복
                t.append(num.popleft())  # 큐에서 원소를 빼냄
                pm.append('+')           # 리스트 t 입장에서는 push를 했으니 + 저장
            t.append(num.popleft())      # 사용자가 원하는 원소를 큐에서 빼냄
            pm.append('+')               # 리스트 t 입장에서는 push를 했으니 + 저장
    if s[i] == t[-1]:                    # 사용자가 원하는 수열이 t의 끝 원소에 있다면
        pm.append('-')                   # 리스트 t 입장에서는 pop을 했으니 - 저장
        t.pop()                          # t에서 해당 수를 빼냄
    else:                                # 아니면 NO를 저장하고 종료
        pm = "NO"                        # (사용자가 원하는 원소를 찾기위해 큐에서 빼내는 작업을 했는데도 불구하고
        break                            # 리스트 t에서 이미 꺼낸 값이라는 뜻이고 그 값이 마지막 원소에 없다면
                                         # 사용자가 원하는 수열을 만드는 것이 불가능 함으로 NO를 저장)
    i += 1                               # i값 1 증가 -> 다음 원소 찾기

for i in pm:            # pm의 원소를 하나씩 i에 대입
    if i == "N":        # i가 NO의 N일 경우
        print("NO")     # NO 출력 후 종료
        break
    print(i)            # pm 원소를 하나씩 출력

