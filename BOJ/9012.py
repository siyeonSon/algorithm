# 2023-01-03 20:20:49
# https://www.acmicpc.net/problem/9012

def pprint(stack) :
    if stack == [] :
        print("YES")
    else :
        print("NO")

def vps(str) :
    stack = []
    for s in str :
        if stack == [] :
            stack.append(s)
        elif stack[-1] == '(' and s == ')' :
            stack.pop()
        else :
            stack.append(s)
    pprint(stack)

n = int(input())
for _ in range(n) :
    str = input()
    vps(str)