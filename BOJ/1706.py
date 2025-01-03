# 2025-01-04 00:04:37
# https://www.acmicpc.net/problem/1706

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = []
rev_board = [''] * c
for _ in range(r) :
    INPUT = input().rstrip()
    board.append(INPUT)
    for i in range(c) :
        rev_board[i] += INPUT[i]

words = []
for alps in board :
    for word in alps.split('#') :
        if len(word) > 1 :
            words.append(word)

for alps in rev_board :
    for word in alps.split('#') :
        if len(word) > 1 :
            words.append(word)

print(sorted(words)[0])