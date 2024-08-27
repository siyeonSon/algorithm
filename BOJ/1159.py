# 2024-08-27 11:03:12
# https://www.acmicpc.net/problem/1159

import sys
input = sys.stdin.readline

n = int(input())
name = []
for _ in range(n) :
    name.append(input().strip())

dic = {}
for n in name :
    if n[0] in dic :
        dic[n[0]] += 1
    else :
        dic[n[0]] = 1

answer = ""
surrender = "PREDAJA"
for k, v in dic.items() :
    if v >= 5 :
        answer += k

if answer :
    print("".join(sorted(answer)))
else :
    print(surrender)