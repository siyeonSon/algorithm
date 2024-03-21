# 2024-03-21 16:46:34
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    answer = 0
    tan_max = max(tangerine)
    tan_cnt = [0 for _ in range(tan_max+1)]
    for t in tangerine :
        tan_cnt[t] += 1
    
    tan_cnt.remove(0)
    tan_cnt.sort(reverse = True)
    
    amount = 0
    for i in range(len(tan_cnt)) :
        amount += tan_cnt[i]
        if amount >= k :
            answer = i+1
            break

    return answer