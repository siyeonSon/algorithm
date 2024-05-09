# 2024-05-09 19:47:02
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    stack = []
    for ss in s :
        if ss == "(" :
            stack.append(ss)
        else : 
            if stack[-1:] == ["("] :
                stack.pop()
            else :
                return False    
    if stack :
        return False

    return True