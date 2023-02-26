# 2023-02-26 14:19:41
# https://www.acmicpc.net/problem/1080

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]

# (x, y)를 기준으로 3X3 행렬 원소 뒤집기
def reverse(x, y) :
    for i in range(x, x+3) :
        for j in range(y, y+3) :
            a[i][j] = 1 - a[i][j]

# a와 b가 같은 행렬인지 비교
def check() :
    for i in range(n) :
        for j in range(m) :
            if a[i][j] != b[i][j] :
                return False
    return True

ans = 0
for i in range(n-2) :
    for j in range(m-2) :
        if a[i][j] != b[i][j] :
            reverse(i, j)
            ans += 1

print(ans if check() else -1)