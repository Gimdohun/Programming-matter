# boj 24463번 문제 - 미로 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.03   #
from collections import deque # 큐를 사용하기 위함
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n, m = map(int,input().split()) # 미로의 크기를 입력받음(N*M)
d1 = [[0] * m for i in range(n)] # s1에서 s2로 가는 경우의 거리를 저장할 배열을 맵 크기만큼 초기화
d2 = [[0] * m for i in range(n)] # s2에서 s1로 가는 경우의 거리를 저장할 배열을 맵 크기만큼 초기화
graph = [] # 맵을 받기 위한 배열초기화

s1 = (-1,-1) # 첫번째 시작위치 혹은 도착위치를 (x,y)로 저장(초기값 = (-1,-1))
s2 = (-1,-1) # 두번째 시작위치 혹은 도착위치를 (x,y)로 저장(초기값 = (-1,-1))
for i in range(n): # 0 ~ n-1까지 반복
    way = list(input()) # 리스트를 받아 way에 저장
    if way[0] == '.': # way의 첫번째 위치에(맨 왼쪽에) 길이있다면(출발 혹은 도착위치)
        if s1 == (-1,-1): # s1에 갱신한 데이터가 없다면
            s1 = (0,i) # s1 갱신
        else: # s1을 이미 갱신했었다면
            s2 = (0,i) # s2 갱신
    elif way[m - 1] == '.': # 마지막 위치에(맨 오른쪽) 길이있다면(출발 혹은 도착위치)
        if s1 == (-1,-1): # s1에 갱신한 데이터가 없다면
            s1 = (m-1,i) # s1 갱신
        else: # s1을 이미 갱신했다면
            s2 = (m-1,i) # s2 갱신

    if i == 0 or i == n-1: # i가 첫번째 혹은 마지막위치에
        if '.' in way: # 길이있다면
            for j in range(m): # 0 ~ m - 1까지 반복
                if way[j] == '.': # 길이 있는지 확인
                    if s1 == (-1,-1): # s1이 갱신되어 있지않다면
                        s1 = (j,i) # s1 갱신
                    else: # s1이 이미 갱신되어있다면
                        s2 = (j,i) # s2 갱신

    graph.append(way) # 입력된 길 혹은 벽을 graph에 대입

def bfs(s,n,m,distance,b,a): # 시작위치, 맵크기(가로), 맵크기(세로), 길의 이동 거리를 담을 인덱스,
    # 길을 뜻하는 문자, 이미 체크했음을 뜻하는 문자
    dx = [0,0,-1,1] # 상, 하, 좌, 우
    dy = [-1,1,0,0] # 상, 하, 좌, 우
    q = deque() # q를 큐로 선언
    q.append((s[0],s[1])) # 시작 위치(x,y)를 담음
    graph[s[1]][s[0]] = a # 시작 위치 방문 설정
    distance[s[1]][s[0]] = 1 # 시작하는 곳까지의 거리 = 1(처음 비용)
    while q: # q가 빌때까지
        x,y = q.popleft() # q에서 값을 뺀 후 변수 x,y에 담음
        for i in range(4): # 0 ~ 3까지 반복(상,하,좌,우 네방향 검색)
            nx = x + dx[i] # x 위치에서 상,하,좌,우 중 한 곳으로 이동했을 때의 위치를 nx에 담음
            ny = y + dy[i] # y 위치에서 상,하,좌,우 중 한 곳으로 이동했을 때의 위치를 ny에 담음
            if 0 > nx or nx >= m or 0 > ny or ny >= n: # 맵을 이탈할경우
                continue # 다른 방향 확인
            if graph[ny][nx] != b: # 길이 아닐경우
                continue # 다른방향 확인
            graph[ny][nx] = a # 그 방향으로 갈 경우 방문처리
            distance[ny][nx] = distance[y][x] + 1 # 원래 있던 위치에서 한칸 갔으니 + 1
            q.append((nx,ny)) # q에 이동 후 위치를 입력

bfs(s1,n,m,d1,'.','1') # s1 시작위치 기준으로 최소비용을 측정(길 == '.', 이미 체크한 곳 = '1')
bfs(s2,n,m,d2,'1','.') # s2 시작위치 기준으로 최소비용을 측정(이미 체크한 곳 == '.', 길 = '1')

sum_value = d1[s1[1]][s1[0]] + d2[s1[1]][s1[0]] # 두 위치에서 든 비용의 합계를 구함
# (시작 혹은 도착 위치는 미로의 불필요한 길이 아니므로 시작 혹은 도착 위치 기준으로 탐색)

for i in range(n): # 0 ~ n - 1까지 반복
    for j in range(m): # 0 ~ m - 1까지 반복
        d = d1[i][j] + d2[i][j] # d1에 입력된 거리(비용)과 d2에 입력된 거리(비용)을 더함
        if graph[i][j] == '+': # 맵에 원래 벽인경우
            print('+',end='') # 벽을 출력
        elif d == sum_value: # d1과 d2의 해당 인덱스 배열이 불필요한 길이 아니라면
            print('.',end='') # 길 출력
        else: # 불필요한 길이라면
            print('@',end='') # @출력
    print() # 개행

