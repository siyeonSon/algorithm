# 2024-02-18 20:59:41
# https://www.acmicpc.net/problem/1120

import sys
input = sys.stdin.readline

a, b = input().split()

def find_difference(str1, str2) :
    cnt = 0
    for i in range(len(str1)) :
        if str1[i] != str2[i] :
            cnt += 1
    return cnt

difference = []
len_a = len(a)
len_b = len(b)
len_diff = len_b - len_a
for i in range(len_diff + 1) :
    difference.append(find_difference(a, b[i:i+len_a]))

print(min(difference))