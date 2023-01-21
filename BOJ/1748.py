# 2023-01-21 15:56:41
# https://www.acmicpc.net/problem/1748

import sys
input = sys.stdin.readline

answer = 0
n = int(input())

length = len(str(n))

# 한 자리 수 작은 수들을 더함 - 예: 100 -> 1~99까지 더함. 99 -> 1~9까지 더함
for i in range(length-1) :
    answer += 9 * 10**i * (i+1)

# 해당 자리 수들을 더함 - 예: 100 -> 3. 99 -> 180 (10~99)
if length > 1 :
    answer += (n - int('9'*(length-1))) * length
else :
    answer += n

print(answer)