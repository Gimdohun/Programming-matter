# boj 18111번 문제 - 마인크래프트 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n,m,b = map(int,input().split()) # 세로, 가로, 블럭의 개수 출력
graph = [list(map(int,input().split())) for i in range(n)] # 그래프에 각 칸의 블럭의 개수를 받음

INF = int(1e9) # 10억을 무한으로 설정
time = INF # time의 초기값은 무한
high = 0 # 가장 높은 곳은 0으로 초기화

# 맵 전체에 블럭이 0칸부터 256칸까지 쌓는 경우 브루트포스
for k in range(257): # 0 ~ 256까지 반복
    total = 0 # 총 시간 = 0으로 초기화
    block = b # 블럭 개수 대입
    for i in range(n): # 0 ~ n - 1까지 반복
        for j in range(m): # 0 ~ m - 1까지 반복
            if k > graph[i][j]: # 쌓인 블럭이 도달해야되는 블럭보다 작다면
                a = k - graph[i][j] # 도달해야하는 높이 - 현재 높이 = 쌓을 블럭의 개수
                total += a # 그 전까지 소요한 시간 + 블럭을 쌓는 시간(시간은 블럭 개수 * 1인데, *1은 변함없으니 생략)
                block -= a # 블럭을 쌓은만큼 사용함
            elif k < graph[i][j]: # 쌓인 블럭이 도달해야되는 블럭보다 크다면
                a = graph[i][j] - k # 현재 블럭 개수 - 도달해야되는 블럭 = 부술 블럭 개수
                total += (a * 2) # 그 전까지 소요한 시간 + (부술 블럭 개수 * 2) (= 걸리는 시간)
                block += a # 블럭을 캔만큼 얻음
    if block < 0: # 블럭이 0보다 작다면(해당 높이까지 쌓을 수 없음)
        total = INF # 총 시간을 무한으로 셋팅 (= 사용 불가능)
    if time >= total: # 지금까지 측정된 최단시간보다 해당 칸까지 쌓은 시간이 더 작거나 같다면
        time,high = total,k # 시간과 높이 초기화

print(time,high) # 시간 높이 출력