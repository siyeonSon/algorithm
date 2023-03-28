# 2023-03-28 22:51:07
# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

sx = sorted(list(set(x)))
dic = {sx[i] : i for i in range(len(sx))}

# list.index(i) 대신에 딕셔너리의 {key, value} 값을 사용하여 사전처럼 조회
for x_ in x:
    print(dic[x_], end = ' ')