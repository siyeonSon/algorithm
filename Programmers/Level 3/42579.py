# 2024-05-08 15:09:38
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    
    # 장르 내림차순
    g_cnt = {}
    s_len = len(genres)
    for i in range(s_len) :
        if genres[i] in g_cnt :
            g_cnt[genres[i]] += plays[i]
        else :
            g_cnt[genres[i]] = plays[i]
    g_cnt = sorted(g_cnt.items(), key=lambda x : -x[1])
    
    # 노래 내림차순, 고유 번호가 낮은 노래를 먼저 수록
    for i in range(len(g_cnt)) :
        p_cnt = []
        genre = g_cnt[i][0]
        for j in range(s_len) :
            if genres[j] == genre :
                p_cnt.append([plays[j], j])
        p_cnt = sorted(p_cnt, key=lambda x : (-x[0], x[1]))
        
        # 수록
        if len(p_cnt) >= 2 :
            for i in range(2) :
                answer.append(p_cnt[i][1])
        else :
            answer.append(p_cnt[0][1])
    return answer