# 2024-08-30 11:09:29
# https://www.acmicpc.net/problem/2559

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tem = list(map(int, input().split()))

answer = []
answer.append(sum(tem[:k]))

for i in range(n-k) :
    answer.append(answer[i] - tem[i] + tem[i+k])

print(max(answer))