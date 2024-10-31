# 2024-10-30 20:29:12
# https://www.acmicpc.net/problem/4889

import sys
input = sys.stdin.readline    

number = 0
while True :
    number += 1
    str = input().strip()
    if '-' in str :
        break
    stack = []
    for s in str :
        if stack :
            if stack[-1] == '{' and s == '}' :
                stack.pop(-1)
                continue
        stack.append(s)

    answer = len(stack)
    if answer != 0 :
        cnt = 0
        for i in range(answer//2) :
            if stack[2*i] == stack[2*i+1] :  # '{{' 혹은 '}}'
                cnt += 1
            else :  # '}{'
                cnt += 2
        answer = cnt
    print("%d. %d" %(number, answer))