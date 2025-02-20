# 2025-02-20 16:10:25
# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    answer = 0
    while True :
        if n == 0 :
            break
        answer += n%2
        n //= 2
    return answer