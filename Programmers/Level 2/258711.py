# 2024-03-19 16:27:04
# https://school.programmers.co.kr/learn/courses/30/lessons/258711

def solution(edges):
    answer = []
    n = max(map(max, edges))  # 정점의 개수
    in_cnt = [0 for _ in range(n+1)]
    out_cnt = [0 for _ in range(n+1)]
    
    vertex = -1
    donut, line, eight = 0, 0, 0
    
    for x, y in edges :
        in_cnt[x] += 1
        out_cnt[y] += 1
    
    for i in range(n) :
        # 정점
        if in_cnt[i] >= 2 and out_cnt[i] == 0 :
            vertex = i
        # 막대 모양 그래프
        if in_cnt[i] == 0 and out_cnt[i] >= 1 :
            line += 1
        # 8자 모양 그래프
        if in_cnt[i] == 2 and out_cnt[i] >= 2 :
            eight += 1

    # 도넛 모양 그래프
    donut = in_cnt[vertex] - line - eight
        
    answer = [vertex, donut, line, eight]
    return answer