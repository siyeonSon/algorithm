# 2023-05-06 21:16:37
# https://www.acmicpc.net/problem/1916

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]
for _ in range(m) :
    start, end, cost = map(int, input().split())
    bus[start].append([end, cost])

start, end = map(int, input().split())  # 목표 비용 경로(출발지, 도착지)

distnace = [1E9] * (n+1)
distnace[start] = 0

def dijkstra(start, end) :
    heap = []
    heappush(heap, [0, start])  # 힙에 시작지점 추가
    while heap :
        weight, index = heappop(heap)
        if weight > distnace[index] :  # 처리 안 해주면 시간 초과 발생
            continue
        for e, c in bus[index] :
            if distnace[e] > weight + c :
                distnace[e] = weight + c
                heappush(heap, [weight+c, e])
    return distnace[end]

print(dijkstra(start, end))