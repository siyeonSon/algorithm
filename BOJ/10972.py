# 2023-01-21 18:58:21
# https://www.acmicpc.net/problem/10972

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
nums = tuple(map(int, input().split()))

pers = list(permutations([i+1 for i in range(n)], n))
length = len(pers)
for i in range(length) :
    if i == length-1 :
        print(-1)
        break
    if pers[i] == nums :
        for p in pers[i+1] :
            print(p, end=" ")
        break