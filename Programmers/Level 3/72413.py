# 2025-02-27 11:28:23
# https://school.programmers.co.kr/learn/courses/30/lessons/72413

from heapq import heappop, heappush

def dijkstra(start, graph) :
    dist = [float('inf')] * (len(graph)+1)
    dist[start] = 0  # 자기 자신 제외
    
    heap = []
    heappush(heap, [0, start])  # 누적거리, 인덱스
    while heap :
        weight, index = heappop(heap)
        if weight > dist[index] :  # 시간 초과 방지
            continue
        for e, c in graph[index] :  # 해당 index에서 갈 수 있는 정점들
            if dist[e] > weight + c :  # 거리가 더 짧으면
                dist[e] = weight + c
                heappush(heap, [weight + c, e])
    return dist

def solution(n, s, a, b, fares):
    answer = 0
    # 지점개수: n, 출발: s, 도착: a b
    graph = [[] for _ in range(n+1)]
    for fare in fares :
        start, end, cost = fare
        graph[start].append([end, cost])
        graph[end].append([start, cost])

    answer = float('inf')
    for i in range(1, n+1) :  # 모든 지점(i)을 경유지로 고려
        dist = dijkstra(i, graph)  # i에서 출발하는 최소 비용
        answer = min(answer, dist[s] + dist[a] + dist[b])  # s→i (합승) + i→a + i→b
    return answer