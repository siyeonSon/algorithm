# 2025-02-24 22:05:05
# https://www.acmicpc.net/problem/1239

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def count(nums) :
    result = 0
    sum_ = 0
    line = []  # 누적합
    for n in nums :
        sum_ += n
        line.append(sum_)
    # 50만큼 떨어진 다른 선이 존재하는 경우 찾기
    for i in range(len(nums)) :
        for j in range(i+1, len(nums)) :
            if line[i] + 50 == line[j] :
                result += 1
    return result

answer = 0
if max(nums) <= 50 :
    for p in permutations(nums) :
        answer = max(answer, count(p))
print(answer)