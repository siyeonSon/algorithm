# 2023-02-22 15:25:45
# https://www.acmicpc.net/problem/1916

import sys
input = sys.stdin.readline

n = int(input())  # 도시의 수
m = int(input())  # 버스의 수
bus = []  # 출발점, 도착점, 비용
for _ in range(m) :
    bus.append(list(map(int, input().split())))
start, end = map(int, input().split())  # 구하고자 하는 출발점와 도착점
start, end = start - 1, end - 1

graph = [[100_000] * n for _ in range(n)]
for i in range(m) :
    graph[bus[i][0]-1][bus[i][1]-1], graph[bus[i][1]-1][bus[i][0]-1] = bus[i][2], bus[i][2]
for i in range(n) :
    graph[i][i] = 0

for i in range(start+1, end+1) :
    tmp = []
    for j in range(start, i) :
        tmp.append(graph[start][j] + graph[j][i])
    graph[start][i] = min(tmp)

print(graph[start][end])