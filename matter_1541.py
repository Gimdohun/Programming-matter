# boj 1541번 문제 - 잃어버린 괄호 #
#     작성자 : 김도훈    #
#   날짜 : 2022.06.29   #
cal = str(input()) # 문자열로 수식을 받음
minus = [[] for i in range(50)] # 마이너스할 값
plus = [[] for i in range(50)] # 플러스 할 값
m = -1 # m은 마이너스 기호가 나올 때도 1을 증가시켜줘야되는데, 처음 마이너스가 나올 때는 아무값도 없는 상태로 1증가 시키면
# 인덱스가 0이 아닌 1부터 시작하므로 -1에서 시작
c = 0 # c는 마이너스가 나왔는지 여부(한번이라도 나왔으면 그 뒤로는 전부다 마이너스 배열이다)
p = 0 # p는 플러스 인덱스 배열
s = 0 # s는 합
for i in cal:
    if i == '-': # 마이너스가 나올경우
        c = 1 # 그 뒤부터는 모두 마이너스 배열
        minus[m] = ''.join([str(n) for n in minus[m]]) # 앞에 인덱스의 리스트를 문자열로 만들어줌
        m += 1 # 마이너스 값 추가
    elif i == '+': # 플러스가 나올 경우
        if c == 1: # 마이너스가 한번이라도 나온 경우
            minus[m] = ''.join([str(n) for n in minus[m]]) # 앞에 인덱스의 리스트를 문자열로 만들어줌
            m += 1 # 마이너스 값 추가
        else:
            plus[p] = ''.join([str(n) for n in plus[p]]) # 앞에 인덱스의 리스트를 문자열로 만들어줌
            p += 1 # 플러스 값 추가
    else: # 자연수가 나온경우(0~9)
        if c == 1: # 마이너스가 한번이라도 나왔다면
            minus[m].append(i) # 마이너스 배열에 추가
        else: # 플러스만 나왔다면
            plus[p].append(i) # 플러스 배열 추가

minus[m] = ''.join([str(n) for n in minus[m]]) # 마지막 인덱스의 리스트를 문자열로 만들어줌
plus[p] = ''.join([str(n) for n in plus[p]]) # 마지막 인덱스의 리스트를 문자열로 만들어줌

for i in range(0,max(p,m)+1): # 0에서 플러스 배열이나 마이너스 배열중 가장 큰 배열까지
    if p >= i: # 플러스 배열이 남아있을 경우
        s += int(plus[i]) # s에 해당 값 플러스
    if m >= i: # 마이너스 배열이 남아있을 경우
        s -= int(minus[i]) # s에 해당 값 마이너스

print(s) # 출력

