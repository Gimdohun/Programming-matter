# boj 2458번 문제 - 키 순서 #
#      작성자 : 김도훈      #
#    날짜 : 2022.06.28     #
import heapq
import sys

input = sys.stdin.readline # input을 빠르게 받기 위함

# n = 노드의 개수, m = 간선의 개수
n, m = map(int,input().split())
# 자신의 노드보다 키가 큰 노드 저장(초기값)
high = [[] for i in range(n + 1)]
# 자신의 노드보다 키가 작은 노드 저장(초기값)
low = [[] for i in range(n + 1)]
# 자신의 노드보다 키가 큰 노드 저장(변경값)
sl = [[] for i in range(n + 1)]
# 자신의 노드보다 키가 작은 노드 저장(변경값)
sh = [[] for i in range(n + 1)]
# 키 순위를 알 수 있는 노드 개수
count = 0
for i in range(m): # 노드 정보를 받음
    a, b = map(int,input().split())
    high[a].append(b) # b 노드가 a 노드보다 크므로 a 노드보다 큰 원소를 담는 인덱스에 저장
    low[b].append(a) # a 노드가 b 노드보다 작으므로 b 노드보다 작은 원소를 담는 인덱스에 저장

for i in range(1, n + 1):
    h = []
    heapq.heappush(h,i)
    while h: # h가 빌 때까지
        now = heapq.heappop(h) # now에 i 노드 보다 큰 노드들이 차례대로 들어감
        for j in high[now]:
            if j not in sh[i]: # i 노드 보다 큰 키를 저장하는 리스트에 j가 없으면 if문 조건 충족
                sh[i].append(j) # 큰 키 목록에 j 노드 저장
                heapq.heappush(h,j)
    l = []
    heapq.heappush(l,i)
    while l: # l이 빌 때까지
        now = heapq.heappop(l)  # now에 i 노드 보다 작은 노드들이 차례대로 들어감
        for j in low[now]: #
            if j not in sl[i]:  # i 노드 보다 작은 키를 저장하는 리스트에 j가 없으면 if문 조건 충족
                sl[i].append(j) # 작은 키 목록에 j 노드 저장
                heapq.heappush(l,j)
    # 큰 키를 가진 노드를 담은 리스트(최종값)의 길이 + 작은 키를 가진 노드를 담은 리스트(최종값)
    # == n- 1(전체 노드의 개수 - 자기자신노드) -> 자신보다 크거나 작은 노드의 정보를 모두 담고 있는 노드는 자신의 순위를 알 수 있다.
    if len(sh[i]) + len(sl[i]) == n - 1:
        # count 1증가
        count += 1

# count 출력
print(count)
