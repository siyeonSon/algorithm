# 2025-02-26 18:33:32
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter

def solution(N, stages):
    rates = []    
    user = len(stages)
    cnt = Counter(stages)
    for i in range(1, N+1) :
        if i in cnt :
            rates.append([i, cnt[i]/user])
            user -= cnt[i]
        else :
            rates.append([i, 0])
    answer = [idx for idx, _ in sorted(rates, key=lambda x : (-x[1], x[0]))] 
    return answer