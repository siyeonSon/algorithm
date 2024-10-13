# 2024-10-13 17:10:44
# https://www.acmicpc.net/problem/1613

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
available = [[False]*n for _ in range(n)]
for _ in range(k) :
    a, b = map(int, input().split())
    available[a-1][b-1] = True

for k in range(n) :  # 경유지
    for i in range(n) :  # 시작
        for j in range(n) :  # 도착
            if not available[i][j] and available[i][k] and available[k][j] :
                available[i][j] = available[i][k] and available[k][j]

s = int(input())
for _ in range(s) :
    a, b = map(int, input().split())
    answer = 0
    if available[a-1][b-1] :
        answer = -1
    elif available[b-1][a-1] :
        answer = 1
    print(answer)

# 재귀로 하였으나 시간초과가 발생함 -> 플로이드 와샬 활용
# 플로이드 와샬 알고리즘의 3중 for문으로 인해 python으로 제출하면 시간초과가 발생함 -> pypy로 제출함
# python으로 제출하기 위해 Dijkstra와 같은 다른 알고리즘을 알아보자