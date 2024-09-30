# 2024-09-30 13:54:14
# https://www.acmicpc.net/problem/10709

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
board = []
for _ in range(h) :
    board.append(list(input().strip()))

answer = [[-1]*w for _ in range(h)]
for i in range(h) :
    for j in range(w) :
        if board[i][j] == "c" :
            answer[i][j] = 0
            for k in range(1, w-j) :
                answer[i][j+k] = k

def pprint(arr) :
    for a in arr :
        print(*a)

pprint(answer)