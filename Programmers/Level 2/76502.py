# 2025-02-24 20:31:34
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    for i in range(len(s)) :        
        answer += isPerfectStr(s[i:]+s[:i])
    return answer

def isPerfectStr(arr) :
    stack = []
    for a in arr :
        if stack :
            if stack[-1] == '[' and a == ']' or stack[-1] == '{' and a == '}' or stack[-1] == '(' and a == ')' :
                stack.pop()
                continue
        stack.append(a)
    return stack == []