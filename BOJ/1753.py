# 2023-05-06 21:55:19
# https://www.acmicpc.net/problem/1753

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e) :
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

distance = [1E9] * (v+1)
distance[k] = 0

def dijkstra(k) :
    heap = []
    heappush(heap, (0, k))
    while heap :
        weight, index = heappop(heap)
        if weight > distance[index] :
            continue
        for e, c in graph[index] :
            if distance[e] > weight + c :
                distance[e] = weight + c
                heappush(heap, (weight+c, e))
dijkstra(k)

for i in range(1, v+1) :
    if distance[i] == 1E9 :
        print('INF')
    else :
        print(distance[i])