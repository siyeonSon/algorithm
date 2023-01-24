# 2023-01-24 21:12:50
# https://www.acmicpc.net/problem/10974

import itertools
import sys
input = sys.stdin.readline

# itertools.permutations() 사용
n = int(input())
nums = [i for i in range(1, n+1)]
for per in itertools.permutations(nums, n) :
    print(*per)


# 백트래킹 사용
n = int(input())
s = []
def dfs() :
    if len(s) == n :
        print(*s)
        return 

    for i in range(1, n+1):
        if not i in s :
            s.append(i)
            dfs()
            s.pop()
dfs()