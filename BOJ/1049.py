# 2023-02-19 14:08:43
# https://www.acmicpc.net/problem/1049

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
guitar = [list(map(int, input().split())) for _ in range(m)]

ans = []
for i in range(m) :
    cost = (n//6) * guitar[i][0]
    left = [(n%6) * guitar[j][1] for j in range(m)]
    ans.append(cost + min(left))

    ans.append((n//6+1) * guitar[i][0])
    ans.append(n * guitar[i][1])

print(min(ans))