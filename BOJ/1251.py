# 2024-11-01 14:33:14
# https://www.acmicpc.net/problem/1251

import sys
input = sys.stdin.readline

word = input().rstrip()
len_w = len(word)
answer = []
for i in range(1, len_w-2) :
    for j in range(i+1, len_w) :
        answer.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])
answer.sort()
print(answer[0])