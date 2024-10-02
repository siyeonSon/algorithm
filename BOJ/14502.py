# 2024-09-30 14:22:58
# https://www.acmicpc.net/problem/14502

import copy
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def combi(board) :
    c_list = []
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :
                c_list.append([i, j])
    return list(combinations(c_list, 3))

def dfs(n_board, x, y) :
    n_board[x][y] = 2
    for i in range(4) :
        nx, ny = dx[i]+x, dy[i]+y
        if 0 <= nx < n and 0 <= ny < m :
            if n_board[nx][ny] == 0 :
                dfs(n_board, nx, ny)

def score(n_board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if n_board[i][j] == 0 :
                cnt += 1
    return cnt

answer = []
for com in combi(board) :
    n_board = copy.deepcopy(board)
    for wall in com :
        n_board[wall[0]][wall[1]] = 1
    for i in range(n) :
        for j in range(m) :
            if n_board[i][j] == 2 :
                dfs(n_board, i, j)
    answer.append(score(n_board))

print(max(answer))