# 2023-02-19 10:35:24
# https://www.acmicpc.net/problem/1182

import sys
input = sys.stdin.readline
from itertools import combinations

ans = 0
n, s = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(1, n+1) :
    for c in combinations(nums, i) :
        if sum(c) == s :
            ans += 1
print(ans)