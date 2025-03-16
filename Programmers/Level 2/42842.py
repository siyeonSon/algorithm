# 2025-03-15 17:52:19
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

import math

def solution(brown, yellow):
    answer = [0, 0]
    for i in range(int(math.sqrt(yellow))+1, 0, -1) :
        if yellow % i == 0 :
            if brown + yellow == (yellow//i+2) * (i+2) :
                answer = [yellow//i + 2, i + 2]
    return answer