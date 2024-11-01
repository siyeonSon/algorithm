# 2024-10-31 22:34:55
# https://www.acmicpc.net/problem/2002

import sys
input = sys.stdin.readline

## 풀이 1
n = int(input())
be, af = [], []
for _ in range(n) :
    be.append(input().strip())
for _ in range(n) :
    af.append(input().strip())

def isOverTake(preCar, carList) :
    for car in preCar :
        if car not in carList :
            return True
    return False

answer = 0
for i in range(n) :
    if isOverTake(be[:i], af[:af.index(be[i])]) :
        answer += 1
print(answer)


## 풀이 2
n = int(input())
IN = [input() for _ in range(n)]

answer = 0
for _ in range(n):
    car = input()
    if IN[0] != car:
        answer += 1
    IN.remove(car)
print(answer)