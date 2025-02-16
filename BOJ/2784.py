# 2025-02-16 21:20:45
# https://www.acmicpc.net/problem/2784

from itertools import permutations
import sys
input = sys.stdin.readline

strs = []
for _ in range(6) :
    strs.append(input().rstrip())

def solve(strs) :
    answers = []
    for p in permutations(strs, 3) :
        puzzle = list(p) + [p[0][i] + p[1][i] + p[2][i] for i in range(3)]
        c_puzzle = list(puzzle)
        for s in strs :
            if s not in c_puzzle :
                break
            c_puzzle.remove(s)
        if c_puzzle == [] :
            answers.append(puzzle)
    if answers :
        return answers
    return 0

answers = solve(strs)
if answers :
    answers.sort()
    print(*answers[0][:3], sep="\n")
else :
    print(answers)