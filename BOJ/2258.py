# 2024-04-04 20:37:13
# https://www.acmicpc.net/problem/2258

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
meats = [list(map(int, input().split())) for _ in range(n)]

# [무게, 가격]
s_meats = sorted(meats, key = lambda x: (x[1], -x[0]))

answer = sys.maxsize
sum_weight, same_price = 0, 0  # 누적합
for i in range(n) :
    weight, cost = s_meats[i]
    sum_weight += weight
    if i > 0 and s_meats[i][1] == s_meats[i-1][1] :  # 가격이 같은 고기는 덤이 아님
        same_price += s_meats[i][1]
    else :
        same_price = 0
    if sum_weight >= m :
        answer = min(answer, s_meats[i][1] + same_price)

if answer == sys.maxsize :
    answer = -1
print(answer)