# 2024-04-18 00:57:21
# https://www.acmicpc.net/problem/2036

import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

pos = []
one = []
neg = []
for s in sequence :
    if s > 1 :
        pos.append(s)
    elif s == 1 :
        one.append(s)
    else :
        neg.append(s)
pos.sort()
neg.sort(reverse=True)

def get_max_score(sequence) :
    score = 0
    while sequence :
        x = sequence.pop()
        if sequence :  # 수열이 남은 경우
            y = sequence.pop()
            score += x*y
        else :
            score += x
    return score

answer = get_max_score(pos) + get_max_score(neg) + len(one)
print(answer)