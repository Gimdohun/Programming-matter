# boj 15829번 문제 - hashing #
#     작성자 : 김도훈    #
#   날짜 : 2022.07.04   #
import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위함

n = int(input()) # 알파벳 개수
l = list(input()) # 알파벳
s = 0
for i in range(n): # 0 ~ n까지 반복
    s += (ord(l[i]) - 96) * (31**i) # 알파벳의 위치(a = 1, b = 2 ...) * (31^알파벳 인덱스 위치)
    s %= 1234567891 # 서로소 숫자
print(int(s)) # 결과 출력