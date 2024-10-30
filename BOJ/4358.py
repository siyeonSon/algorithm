# 2024-10-30 20:02:44
# https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin.readline

cnt = 0
dic = {}
while True :
    name = input().strip()
    if name == '':
        break
    cnt += 1
    if name in dic :
        dic[name] += 1
    else :
        dic[name] = 1

s_dic = dict(sorted(dic.items()))

for k, v in s_dic.items() :
    print("%s %.4f" %(k, v/cnt*100))