# 2025-02-20 21:11:07
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people)-1
    while True :
        if left > right : break
        if people[left] + people[right] <= limit :
            left += 1
        right -= 1
        answer += 1
    return answer