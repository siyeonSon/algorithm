# 2025-03-15 17:30:56
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    width, length = 0, 0   # width는 length보다 크거나 같다
    for s in sizes :
        width = max(width, max(s[0], s[1]))
        length = max(length, min(s[0], s[1]))
    answer = width * length
    return answer