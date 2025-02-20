# 2025-02-20 22:05:06
# https://school.programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    answer = 0
    
    map = [[float('inf')] * N for _ in range(N)]
    for r in road :
        a, b, c = r
        if c < map[a-1][b-1] :
            map[a-1][b-1] = c
            map[b-1][a-1] = c
    for i in range(N) :
        map[i][i] = 0
    
    for k in range(N) :
        for i in range(N) :
            for j in range(N) :
                map[i][j] = min(map[i][j], map[i][k] + map[k][j])
    
    for i in range(N) :
        if map[0][i] <= K :
            answer += 1
    return answer