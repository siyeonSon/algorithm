# 2025-03-16 16:34:17
# https://www.acmicpc.net/problem/14465

import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
light = [0] * (n+1)
for _ in range(b) :
    light[int(input())] = 1

## 슬라이딩 윈도우
broken = sum(light[1:k+1])
answer = k
for i in range(1, n-k+1) :
    broken = broken - light[i] + light[i+k]
    answer = min(answer, broken)
print(answer)

## 누적합
# prefix = []
# cnt = 0
# for i in range(n+1) :
#     if light[i] == 1 :
#         cnt += 1
#     prefix.append(cnt)

# answer = k
# for i in range(1, n-k+1) :
#     answer = min(answer, prefix[k+i] - prefix[i])
# print(answer)