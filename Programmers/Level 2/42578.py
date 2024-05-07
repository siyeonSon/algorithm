# 2024-05-07 12:32:35
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    c_cnt = {}
    for name, type in clothes :
        if type in c_cnt :
            c_cnt[type] += 1
        else :
            c_cnt[type] = 1
    for k, v in c_cnt.items() :
        answer = answer * (v+1)
    answer = answer - 1   # 아무 것도 입지 않은 경우
    return answer