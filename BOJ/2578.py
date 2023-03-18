# 2023-03-18 21:40:34
# https://www.acmicpc.net/problem/2578

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
calls = [list(map(int, input().split())) for _ in range(5)]

def horizontal() :
    cnt = 0
    for i in range(5) :
        if sum(board[i]) == 0 :
            cnt += 1
    return cnt   

def vertical() :
    cnt = 0
    for i in range(5) :
        ver = 0
        for j in range(5) :
            ver += board[j][i]
        if ver == 0 :
            cnt += 1
    return cnt

def diagonal() :
    cnt, dia1, dia2 = 0, 0, 0
    for i in range(5) :
        dia1 += board[i][i]
        dia2 += board[4-i][i]
    if dia1 == 0 :
        cnt += 1
    if dia2 == 0 :
        cnt += 1
    return cnt

# 빙고 여부 확인
def bingo(board) :
    return horizontal() + vertical() + diagonal()

answer = 0
for i in range(5) :
    for j in range(5) :
        answer += 1
        for b in board :
            if calls[i][j] in b :
                b[b.index(calls[i][j])] = 0
                if bingo(board) >= 3 :
                    print(answer)
                    exit()