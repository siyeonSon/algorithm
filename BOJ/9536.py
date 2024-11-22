# 2024-11-22 12:30:18
# https://www.acmicpc.net/problem/9536

import re
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    mixed = list(input().split())

    sound = []
    while True :
        INPUT = input()
        if INPUT == "what does the fox say?\n" :
            break
        sound.append(list(INPUT.split())[2])

    answer = []
    for m in mixed : 
        if m not in sound :
            answer.append(m)
    print(" ".join(answer))