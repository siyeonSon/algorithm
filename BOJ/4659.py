# 2024-09-27 10:33:26
# https://www.acmicpc.net/problem/4659

import sys
input = sys.stdin.readline

noun = ["a", "e", "i" ,"o" ,"u"]
def isNoun(str) :
    for s in str :
        if s in noun :
            return True
    return False

def solve(str) :
    if not isNoun(str) :  # 조건 1: 모음 하나를 반드시 포함한다
        return False
    stack = []
    for i in range(len(str)) :
        if not stack :
            stack.append(str[i])
            continue
        if str[i] != "e" and str[i] != "o" and str[i-1] == str[i] :  # 조건 2: 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다
            return False
        if isNoun(stack[-1]) == isNoun(str[i]) :  # 자음-자음 혹은 모음-모음인 경우
            if len(stack) >= 2 :  # 조건 3: 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
                return False
            stack.append(str[i])
            continue
        stack = [str[i]]
    if len(stack) == len(str) :
        return True
    return True

while True :
    str = input().strip()
    if str == "end" :
        break
    if solve(str) :
        print(f"<{str}> is acceptable.")
    else :
        print(f"<{str}> is not acceptable.")