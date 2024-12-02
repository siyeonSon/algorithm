# 2024-12-02 15:10:15
# https://www.acmicpc.net/problem/20310

import sys
input = sys.stdin.readline

s = input().rstrip()

cnt0 = s.count('0')
cnt0 //= 2
cnt1 = s.count('1')
cnt1 //= 2

answer = ''
for i in range(len(s)) :
    if s[i] == '0' :  # 0은 뒤에서 부터 제거
        if cnt0 > 0 :
            cnt0 -= 1
            answer += s[i]
    elif s[i] == '1' :  # 1은 앞에서 부터 제거
        if cnt1 > 0 :
            cnt1 -= 1
        else :
            answer += s[i]

print(answer)