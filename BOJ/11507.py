# 2024-11-25 21:24:58
# https://www.acmicpc.net/problem/11507

import sys
input = sys.stdin.readline

s = input().strip()

FAIL = 'GRESKA'
dic = { 'P' : [], 'K' : [], 'H' : [], 'T' : [] }

for i in range(0, len(s), 3) :
    simbal, number = s[i], s[i+1:i+3]
    if number in dic[simbal] :
        print(FAIL)
        exit()
    dic[simbal].append(number)

for key, value in dic.items() :
    print(13 - len(value), end=' ')