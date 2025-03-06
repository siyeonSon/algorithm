# 2025-03-06 18:08:29
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    visited = [[0] * n for _ in range(m)]
    visited[0][0] = 1
    
    for i in range(m) :
        for j in range(n) :
            if [i+1, j+1] in puddles :
                continue
            if i+1 < m :
                visited[i+1][j] += visited[i][j]
            if j+1 < n :
                visited[i][j+1] += visited[i][j]
    return visited[-1][-1] % 1_000_000_007