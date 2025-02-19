# 2025-02-19 16:51:15
# https://school.programmers.co.kr/learn/courses/30/lessons/12952

def solution(n):
    
    def check(ls, new):
        for i in range(len(ls)):
            if new == ls[i] or (len(ls)-i) == abs(ls[i]-new):
                return False
        return True

    def dfs(n, ls):
        if len(ls) == n:
            return 1
        cnt = 0
        for i in range(n):
            if check(ls, i):
                cnt += dfs(n, ls+[i])
        return cnt
        
    return dfs(n, [])

## 시간초과
def n_queen(n, x, queen):  # x: 새로운 퀸의 자리
    result = 0
    if x == n:
        return 1
    for i in range(n):
        queen[x] = i
        if check(x, queen):
            result += n_queen(n, x+1, queen)
    return result

def check(x, queen):
    for i in range(x):
        if queen[x] == queen[i] or abs(x-i) == abs(queen[x] - queen[i]):
            return False
    return True

def solution(n):
    queen = [0] * n  # queen[i]=j -> 체스판의 i행 j열에 퀸을 위치함
    answer = n_queen(n, 0, queen)
    return answer