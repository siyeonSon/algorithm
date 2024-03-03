# 2024-03-03 14:56:04
# https://www.acmicpc.net/problem/21758

import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))

# s[i]: 0~i까지 누적합
s = honey[:]
for i in range(1, n):
    s[i] += s[i-1]

ans = 0
for i in range(1, n-1) :
    ans = max(ans,
            2*s[n-1]-honey[0]-honey[i]-s[i],  # 벌벌꿀: bee1(0), bee2(i), comb(n-1)
            s[n-2]-honey[0]+honey[i],  # 벌꿀벌: bee1(0), comb(i), bee2(n-1)
            s[i-1]+s[n-2]-honey[i])  # 꿀벌벌 : comb(0), bee1(i), bee2(n-1)

print(ans)