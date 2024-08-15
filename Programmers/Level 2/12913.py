# 2024-08-14 16:38:50
# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0
    dp = [0] * 4
    for l in land :
        tmp = dp[:]
        for i in range(4) :
            dp[i] = l[i] + max(tmp[:i] + tmp[i+1:])
    answer = max(dp)
    return answer