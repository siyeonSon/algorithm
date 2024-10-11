# 2024-10-11 21:20:28
# https://www.acmicpc.net/problem/1956

import sys
input = sys.stdin.readline

v, e = map(int, input().split())

matrix = [[float('inf')]*v for _ in range(v)]
for _ in range(e) :
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = c

for i in range(v) :  # 시작
    for j in range(v) :  # 중간
        for k in range(v) :  # 끝
            matrix[i][k] = min(matrix[i][k], matrix[i][j] + matrix[j][k])

answer = float('inf')
for i in range(v) :
    answer = min(answer, matrix[i][i])
if answer < float('inf') :
    print(answer)
else :
    print(-1)