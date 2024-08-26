# 2024-08-26 16:06:51
# https://www.acmicpc.net/problem/10808

import sys
input = sys.stdin.readline

s = input().strip()

answer = [0] * 26
for str in s :
    answer[ord(str)-97] += 1

print(*answer, sep=' ')