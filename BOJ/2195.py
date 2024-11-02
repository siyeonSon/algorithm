# 2024-11-02 19:35:11
# https://www.acmicpc.net/problem/2195

import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

answer = 0
tmp = ''
for str in p :
    if tmp+str not in s :
        answer += 1
        tmp = str
    else :
        tmp += str
if tmp :
    answer += 1
print(answer)