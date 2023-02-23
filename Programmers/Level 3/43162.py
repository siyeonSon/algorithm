# 2023-02-23 20:48:04
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    global visited
    answer = 0
    visited = [False] * n

    # 네트워크 탐색
    for i in range(n) :
        if not visited[i] : 
            answer += dfs(i, n, computers)

    return answer

def dfs(start, n, computers) :
    global visited
    visited[start] = True

    # start 노드와 이어진 다른 노드 탐색
    for end in range(n) :
        if start != end and computers[start][end] == 1 and not visited[end] :
            dfs(end, n, computers)
    return 1