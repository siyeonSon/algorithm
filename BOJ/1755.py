# 2024-11-01 10:49:36
# https://www.acmicpc.net/problem/1755

import math
import sys
input = sys.stdin.readline

a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

m, n = map(int, input().split())
result = []
for i in range(m, n+1) :
    read = ''
    for s in str(i) :
        read += a[int(s)]
    result.append([read, i])
result.sort()

for i in range(len(result)) :
    print(result[i][1], end=" ")
    if i%10 == 9 :
        print()