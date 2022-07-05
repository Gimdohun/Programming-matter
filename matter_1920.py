# boj 1920번 문제 - 수찾기 #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline  # 입력을 빠르게 받기 위함

n = int(input()) # A[n]의 존재 대상의 리스트 원소 개수
array = list(map(int,input().split())) # A[n]의 존재 대상의 리스트
m = int(input()) # 찾는 대상인 A 리스트의 원소 개수
find = list(map(int,input().split())) # 찾는 대상 A의 리스트
s = [0] * m # s를 0으로 m개 리스트로 초기화
array.sort() # A[n]의 존재 대상 리스트 정렬
for i in range(m): # 0 ~ m-1까지 반복
    start = 0 # 시작 = 0(array의 처음 인덱스 번호)
    end = len(array) - 1 # 끝 = array의 길이 - 1 (array의 마지막 인덱스번호)
    while start <= end: # start가 end보다 작거나 같다면 반복
        mid = (start + end) // 2 # 중간값 초기화
        if find[i] == array[mid]: # 찾는 수가 중간 인덱스 원소와 같다면
            s[i] = 1 # 1 : 찾음, 0 : 못찾음
            break # 반복문 종료(더 찾을 필요 없음)
        elif find[i] > array[mid]: # 찾는 수가 중간 인덱스 원소보다 크다면
            start = mid+1 # 시작값을 중간값 다음으로 바꾸어 중간값 다음부터 탐색(그 앞엔 없음)
        else: # 찾는 수가 중간 인덱스 원소보다 작다면
            end = mid-1 # 종료값을 중간값 이전으로 바꾸어 중간값 전부터 탐색(그 뒤엔 없음)

for i in s: # 결과 출력
    print(i)
