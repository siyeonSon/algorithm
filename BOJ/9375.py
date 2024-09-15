# 2024-09-15 23:28:45
# https://www.acmicpc.net/problem/9375

import sys
input = sys.stdin.readline

def solve() :
    m = int(input())
    dic = {}
    for _ in range(m) :
        n, t = input().split()
        if t in dic :
            dic[t] += 1
        else :
            dic[t] = 1

    answer = 1
    for key, value in dic.items() :
        answer *= (value + 1)
    print(answer - 1)

n = int(input())
for _ in range(n) :
    solve()