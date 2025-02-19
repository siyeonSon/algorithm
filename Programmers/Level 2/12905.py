# 2025-02-19 15:09:38
# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    dp = list(board)
    for i in range(1, len(board)) :
        for j in range(1, len(board[i])) :
            if board[i][j] == 1 :
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1
    return max(map(max, board)) ** 2