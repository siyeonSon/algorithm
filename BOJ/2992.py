# 2024-11-02 19:44:59
# https://www.acmicpc.net/problem/2992

from itertools import permutations
import sys
input = sys.stdin.readline

num = input().rstrip()

answer = 0
for per in permutations(sorted(num)) :
    if per[0] >= num[0] :
        new_num = ''.join(per)
        if num < new_num :
            answer = new_num
            break

print(answer)