# 2023-02-19 10:35:24
# https://www.acmicpc.net/problem/1182


## 순열
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


## 백트레킹
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
def dfs(start, sum) :
    global cnt
    if start >= n :  # index를 벗어나면 탈출
        return
    sum += nums[start]
    if sum == s :
        ans += 1
    
    dfs(start+1, sum)  # 해당 원소를 포함하는 경우
    dfs(start+1, sum-nums[start])  # 해당 원소를 포함하지 않는 경우

dfs(0, 0)
print(ans)