# 2023-02-23 10:19:20
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)
    return answer

def dfs(numbers, target, x, cnt) :
    global answer
    if x == len(numbers) :
        if cnt == target :
            answer += 1
        return
    dfs(numbers, target, x+1, cnt+numbers[x])
    dfs(numbers, target, x+1, cnt-numbers[x])