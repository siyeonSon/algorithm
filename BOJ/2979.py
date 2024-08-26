# 2024-08-26 16:36:51
# https://www.acmicpc.net/problem/2979

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

truck = []
for _ in range(3) :
    truck.append(list(map(int, input().split())))

time = [0] * (max(map(max, truck)))

for tr in truck :
    for i in range(tr[0], tr[1]) :
        time[i] += 1

answer = 0
for ti in time :
    if ti == 0 :
        continue
    elif ti == 1 :
        answer += ti * a
    elif ti == 2 :
        answer += ti * b
    else :
        answer += ti * c

print(answer)