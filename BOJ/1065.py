# 2023-02-24 14:02:18
# https://www.acmicpc.net/problem/1065

import sys
input = sys.stdin.readline

def check(num) :
    diff = int(num[0]) - int(num[1])
    for i in range(1, len(num)) :
        if int(num[i-1]) - int(num[i]) != diff :
            return 0
    return 1

answer = 0
n = input()
if int(n) < 10 :
    print(int(n))
else :
    answer += 9
    for i in range(10, int(n)+1) :
        answer += check(str(i))
    print(answer)