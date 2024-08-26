# 2024-08-26 17:00:26
# https://www.acmicpc.net/problem/10988

import sys
input = sys.stdin.readline

str = input().strip()

for i in range(len(str)//2) :
    if str[i] != str[-i-1] :
        print(0)
        exit()
print(1)