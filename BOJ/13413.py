# 2024-11-01 11:22:13
# https://www.acmicpc.net/problem/13413

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    pre = input().rstrip()
    after = input().rstrip()

    w, b = 0, 0
    for i in range(n) :
        if pre[i] != after[i] :
            if pre[i] == 'W' :
                w += 1
            else :
                b += 1
    print(max(w, b))