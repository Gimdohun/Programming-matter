# boj 1654번 문제 - 랜선 자르기 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

k,n = map(int,input().split()) # 가지고 있는 랜선의 개수 = k, 만들어야되는 랜선의 수 = n
s = []
for i in range(k):          # 가지고 있는 랜선의 길이를 리스트에 넣음
    s.append(int(input()))

start = 1                   # 랜선이 0cm일 순 없으니 1cm를 시작값으로 둠
end = max(s)                # 랜선의 최댓값을 종료값으로 둠
max_value = 0               # 만들어야되는 랜선의 개수를 충족 시킨경우 중 가장 큰 길이
while start <= end:         # 시작값이 종료값을 넘지않도록함
    c = 0                   # 랜선의 갯수
    mid = (start + end) // 2 # 시작값 + 종료값의 중간값 설정
    for i in range(k):      # 모든 랜선을 중간값으로 잘랐을 경우 나오는 랜선의 갯수
        c += (s[i] // mid)
    if c >= n:              # 랜선의 갯수가 만들어야되는 랜선의 갯수보다 크거나 같을 때
        max_value = mid     # 가장 큰 길이 = 중앙값
        start = mid + 1     # 중앙값 다음값을 시작값으로 두어 중앙값보다 큰 값부터 탐색
                            # (개수는 충족됬기에 현재까지 나온 가장 큰 길이보다 적은 길이의 경우는 볼필요가 없음)
    else:                   # 랜선의 갯수가 만들어야되는 랜선의 갯수보다 작을 때
        end = mid - 1       # 중앙값 이전값을 종료값으로 두어 중앙값보다 작은 값부터 탐색
                            # (개수가 부족하여 중앙값보다 크거나 같은 값은 가질 수 없음)

print(max_value)            # 최종값 출력