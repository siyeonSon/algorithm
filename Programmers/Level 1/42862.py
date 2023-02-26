# 2023-02-26 11:01:33
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    
    # 학생들이 가진 체육복 개수
    clothes = [1] * n
    for l in lost :
        clothes[l-1] -= 1
    for r in reserve :
        clothes[r-1] += 1
    
    # 2벌인 학생과 0벌인 학생 교체
    for i in range(1, n) :
        if abs(clothes[i-1] - clothes[i]) == 2 : # (0,2) or (2,0) 인 경우
            clothes[i-1], clothes[i] = 1, 1
        
    # 정답 구하기
    for c in clothes :
        if c >= 1 :  # 한 벌 이상 가지고 있는 경우
            answer += 1
    return answer