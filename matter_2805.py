# boj 2805번 문제 - 나무자르기 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n,m = map(int,input().split()) # 나무개수와 필요한 길이 출력
h = list(map(int,input().split())) # 나무들의 길이를 리스트로 담음
start = 0 # 시작값 = 0(나무를 모두 다자를 경우)
end = max(h) # 종료값은 가장 큰 나무의 높이
while start <= end: # 시작값이 종료값을 초과하지 경우까지 반복
    mid = (start + end) // 2 # 시작값과 종료값의 중간값 설정
    c = 0 # 잘라진 나무길이
    for i in h: # h 리스트에 담겨있는 모든 나무를 하나씩 i에 대입
        if i > mid: # i가 중간값보다 클경우
            c += i - mid # mid만큼 자름
    if c >= m: # 잘라진 나무길이가 사용자가 원하는 나무길이보다 크거나 같은 경우
        start = mid + 1 # 시작값을 중간값보다 더 큰값을 가져서 나무를 더 작게 자를 수 있는 경우 확인
        min_value = mid # 현재까지 나온 톱날이 가장 큰 값 = 중간값
    else: # 아닐경우
        end = mid - 1 # 종료값을 중간값보다 낮게잡아 톱날의 길이를 줄임

print(min_value) # 가장 큰 톱날길이(가장 적게 나무를 파기하기 위함) 출력