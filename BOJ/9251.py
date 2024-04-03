# 2024-03-27 14:30:08
# https://www.acmicpc.net/problem/9251

import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

len1, len2 = len(str1), len(str2)

board = [[0] * (len2+1) for _ in range(len1+1)]

for i in range(1, len1+1) :
    for j in range(1, len2+1) :
        if str1[i-1] == str2[j-1] :
            board[i][j] = board[i-1][j-1] + 1
        else :
            board[i][j] = max(board[i-1][j], board[i][j-1])

print(board[-1][-1])