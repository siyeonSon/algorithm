# 2023-02-23 15:43:20
# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boad = [list(input().strip()) for _ in range(n)]

# 다시 칠할 횟수 구하기
def check(boad8x8) :
    color = 0
    for i in range(0, 8, 2) :
        color += (boad8x8[i][0::2].count('W') + boad8x8[i][1::2].count('B') 
                    + boad8x8[i+1][0::2].count('B') + boad8x8[i+1][1::2].count('W'))
    return min(color, 64-color)

cnt = []
# 8X8 체스판 만들기
for i in range(n-7) :
    for j in range(m-7) :
        nboad = []
        for b in boad[i:i+8] :
            nboad.append(b[j:j+8])
        cnt.append(check(nboad))
print(min(cnt))