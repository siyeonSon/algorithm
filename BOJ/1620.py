# 2024-09-15 21:39:35
# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}  # {키: 포켓몬 이름, 밸류: 포켓몬 번호}
arr = [""]
for i in range(n) :
    name = input().strip()
    dic[name] = i+1
    arr.append(name)

for _ in range(m) :
    pro = input().strip()
    if pro.isdigit() :  # 포켓몬 번호 -> 포켓몬 이름
        print(arr[int(pro)])
    else :  # 포켓몬 이름 -> 포켓몬 번호
        print(dic[pro])