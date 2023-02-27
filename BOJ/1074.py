# 2023-02-23 15:39:44
# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

ans = 0
while n > 0 :
    # 2**(n-1)을 기준으로 Z 모양의 위치를 정함
    n -= 1
    if r < 2**n and c < 2**n :  # Z의 0번째 위치
        r, c = r, c
        ans += (2**n)**2 * 0
    elif r < 2**n and c >= 2**n :  # Z의 1번째 위치
        r, c = r, abs(2**n - c)
        ans += (2**n)**2 * 1
    elif r >= 2**n and c < 2**n :  # Z의 2번째 위치
        r, c = abs(2**n - r), c
        ans += (2**n)**2 * 2
    elif r >= 2**n and c >= 2**n :  # Z의 3번째 위치
        r, c = abs(2**n - r), abs(2**n - c)
        ans += (2**n)**2 * 3
print(ans)