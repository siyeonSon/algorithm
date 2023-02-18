# 2023-02-18 14:22:16
# https://www.acmicpc.net/problem/1316

import sys
input = sys.stdin.readline

def isGroupWord(word) :
    stack = [word[0]]
    for w in word : 
        if w != stack[-1] :
            if w in stack :
                return False  # is not group word
            stack.append(w)
    return True  # is group word   

answer = 0
n = int(input())
for _ in range(n) :
    answer += isGroupWord(input())
print(answer)