# 2023-11-22 20:07:37
# https://www.acmicpc.net/problem/2108

from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n) :
    numbers.append(int(input()))

def find_mode(numbers) :
    count = Counter(numbers)
    mode_count = count.most_common()[0][1]
    modes = []
    for key, value in count.items() :
        if value == mode_count :
            modes.append(key)
    if len(modes) > 1 :
        return sorted(modes)[1]
    return modes[0]

answer = []
answer.append(int(round(sum(numbers)/n, 0)))  # 산술평균
answer.append(sorted(numbers)[n//2])  # 중앙값
answer.append(find_mode(numbers))  # 최빈값
answer.append(max(numbers) - min(numbers))  # 범위

print(*answer, sep='\n')