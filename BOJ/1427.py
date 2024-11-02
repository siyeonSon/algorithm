# 2024-11-03 00:57:46
# https://www.acmicpc.net/problem/1427

import sys
input = sys.stdin.readline

n = input().rstrip()
print(''.join(sorted(n, reverse=True)))