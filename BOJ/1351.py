# 2023-02-28 14:30:37
# https://www.acmicpc.net/problem/1351

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

ans = 0
n, p, q = map(int, input().split())
a = dict()  # [1]*(n+1)을 하면 메모리 초과남 -> dictionary 사용
a[0] = 1

def dp(x) :
    global ans
    if x in a :  # x==0 인 경우 && a[x] 값을 전에 구한 경우 재귀를 돌지 않음 -> 시간 초과 감소
        return a[x]
    a[x] = dp(x//p) + dp(x//q)
    return a[x]

dp(n)
print(a[n])