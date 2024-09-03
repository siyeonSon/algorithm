# 2024-09-03 11:58:18
# https://www.acmicpc.net/problem/2075

import heapq
import sys
input = sys.stdin.readline

n = int(input())
graph = []  # 우선순위 큐
# 우선순위 큐의 크기를 n으로 유지하면서 최소값을 제거함

for i in range(n) :
    numbers = map(int, input().split())
    for num in numbers :
        if len(graph) < n :
            heapq.heappush(graph, num)  # 큐에 값 추가
        else :
            if graph[0] < num :
                heapq.heappop(graph)  # 큐의 최솟값 제거
                heapq.heappush(graph, num)  # 큐에 값 추가

print(graph[0])