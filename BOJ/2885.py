# 2024-08-09 14:54:17
# https://www.acmicpc.net/problem/2885

import sys
input = sys.stdin.readline

k = int(input())

# 가장 작은 초콜릿의 크기
size = 1
while True:
    if size >= k : break
    size = size << 1
print(size, end=" ")

# 몇 번 쪼개야 하는지
cnt = 0
while True :
    if k == 0 : break
    if k >= size :
        k -= size
    else : 
        size //= 2
        cnt += 1
print(cnt)