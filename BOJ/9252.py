# 2024-04-09 14:35:11
# https://www.acmicpc.net/problem/9252

import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

len1, len2 = len(str1), len(str2)

def pprint(arr) :
    for a in arr :
        print(a)

# board 생성
def make_board() :
    board = [[0] * (len2+1) for _ in range(len1+1)]
    for i in range(1, len1+1) :
        for j in range(1, len2+1) :
            if str1[i-1] == str2[j-1] :
                board[i][j] = board[i-1][j-1] + 1
            else :
                board[i][j] = max(board[i-1][j], board[i][j-1])
    return board

def find_LCS(board) :
    LCS = ""
    i = len1
    j = len2
    while True :
        if i < 0 or j < 0 :
            break
        if board[i][j] != board[i][j-1] and board[i][j] != board[i-1][j] :
            LCS = str1[i-1] + LCS
            i = i - 1
            j = j - 1
        if board[i][j] == board[i][j-1] :
            j = j - 1
        if board[i][j] == board[i-1][j] :
            i = i - 1
    return LCS


board = make_board()
ans1 = board[-1][-1]
print(ans1)

if ans1 != 0 :
    ans2 = find_LCS(board)
    print(ans2)