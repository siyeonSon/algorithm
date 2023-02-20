# 2023-02-20 14:23:38
# https://www.acmicpc.net/problem/10867

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

print(* sorted(list(set(nums))))