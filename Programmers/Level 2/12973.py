# 2024-03-27 14:23:56
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    for i in range(len(s)) :
        if stack and stack[-1] == s[i] :
            stack.pop()
        else :
            stack.append(s[i])
    if stack :
        return 0
    return 1