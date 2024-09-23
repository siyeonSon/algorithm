# 2024-09-23 12:55:07
# https://www.acmicpc.net/problem/2910

from collections import Counter
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
nums = list(input().split())

dic = Counter(nums)
s_dic = sorted(dic.items(), key = lambda x: -x[1])

answer = ""
for key, value in s_dic :
    answer += (key + " ") * value

print(answer)