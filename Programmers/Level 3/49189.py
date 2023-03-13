# 2023-03-13 18:55:30
# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque
def solution(n, edge):
    answer = 0
    
    distance = [0] * (n+1)
    distance[0], distance[1] = -1, -1  # 0번 노드와 1번 노드에는 방문할 수 없음
    graph = [[] for _ in range(n+1)]
    
    # 노드 간의 관계를 나타내는 그래프 생성
    for ed in edge :
        a, b = ed
        graph[a].append(b)
        graph[b].append(a)
    
    # print(graph)
    # [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]

    # 가장 멀리 떨어진 위치 찾기
    queue = deque()
    queue.append([1, 1])  # 1번 노드, 거리
    while queue :
        x, cnt = queue.popleft()
        for nx in graph[x] :
            if distance[nx] == 0 :
                distance[nx] = cnt
                queue.append([nx, cnt+1])
    
    # 가장 멀리 떨어진 노트가 몇 개인지
    answer = distance.count(max(distance))
    
    return answer


#### 시간 초과 발생 코드
from collections import deque
def solution(n, edge):
    answer = 0
    
    distance = [0] * n
    graph = [[False]*n for i in range(n)]
 
    for ed in edge :
        a, b = ed
        graph[a-1][b-1], graph[b-1][a-1] = True, True
    
    queue = deque()
    queue.append([0, 1])
    distance[0] = 1
    while queue :
        x, cnt = queue.popleft()
        for i in range(n) :  ## 계속 반복문을 도는 것에서 시간 초과 발생
            if distance[i] == 0 and graph[x][i] == True :
                distance[i] = cnt
                queue.append([i, cnt+1])
    
    answer = distance.count(max(distance))
    return answer