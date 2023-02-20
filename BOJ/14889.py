# 2023-02-20 14:39:25
# https://www.acmicpc.net/problem/14889

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
idx = [i for i in range(n)]

def teamwork(t) :
    cnt = 0
    for i in t :
        for j in t :
            cnt += s[i][j]
    return cnt

ans = []
for c in combinations(idx, n//2) :
    t1 = list(c)
    t2 = [i for i in idx if i not in t1]
    ans.append(abs(teamwork(t1)-teamwork(t2)))

print(min(ans))