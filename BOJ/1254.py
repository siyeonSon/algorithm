# 2023-02-24 14:30:54
# https://www.acmicpc.net/problem/1254

import sys
input = sys.stdin.readline

s = input().strip()

for i in range(len(s)) :
    if s[i:] == s[i:][::-1] : # if 순방향 == 역방향
        print(len(s)+i)
        break