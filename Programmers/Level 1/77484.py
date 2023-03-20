# 2023-03-20 15:07:50
# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    
    # 일치 개수
    same_cnt = 0
    for l in lottos :
        if l in win_nums :
            same_cnt += 1
    
    # 0의 개수
    zero_cnt = lottos.count(0)
    
    # 최저 순위
    if same_cnt >= 2 :
        grade = 7 - same_cnt
    else :
        grade = 6
        
    # 최고 순위
    if grade-zero_cnt >= 1 :
        answer = [grade-zero_cnt, grade]
    else :
        answer = [1, grade]

    return answer