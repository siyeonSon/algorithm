# 2024-09-17 23:09:19
# https://www.acmicpc.net/problem/1213

from collections import Counter
import sys
input = sys.stdin.readline

name = input().strip()
cnt = Counter(name)

mid = ""  # 홀수 개수일 때 중간에 들어갈 값
odd_cnt = 0
for k, v in cnt.items() :
    if v % 2 != 0 :  # 홀수
        odd_cnt += 1
        mid = k
        if odd_cnt >= 2 :  # 홀수 2개 이상 -> 팰린드롬 불가
            print("I'm Sorry Hansoo")
            exit()

answer = ""
s_cnt = sorted(cnt.items())
for k, v in s_cnt :
    answer += (k * (v//2))
print(answer + mid + answer[::-1])