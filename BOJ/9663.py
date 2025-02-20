# 2025-02-20 14:23:19
# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

## 코드 1
n = int(input())

# 퀸을 놓을 수 있는가?
def check(y, queen) :
    x = len(queen)
    for i in range(x) :
        if queen[i] == y or abs(i-x) == abs(queen[i]-y) :
            return False
    return True

def n_queen(queen) :
    answer = 0
    if len(queen) == n :
        return 1
    for i in range(n) :  # x행에 퀸을 하나씩 놓음
        if check(i, queen) :
            answer += n_queen(queen+[i])
    return answer

# queen[x] = y -> x번째 행 y열에 퀸이 위치함
print(n_queen([]))

#####
## 코드 2
n = int(input())

answer = 0
queen = [0] * n

# 퀸을 놓을 수 있는가?
def check(x) :
    for i in range(x) :
        if queen[i] == queen[x] or abs(i-x) == abs(queen[i]-queen[x]) :
            return False
    return True

def n_queen(x) :
    global answer
    if x == n :
        answer += 1
        return
    for i in range(n) :  # x행에 퀸을 하나씩 놓음
        queen[x] = i   # queen[x] = y -> x번째 행 y열에 퀸이 위치함
        if check(x) :
            n_queen(x+1)
n_queen(0)
print(answer)