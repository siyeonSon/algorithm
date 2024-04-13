# 2024-04-12 22:46:30
# https://www.acmicpc.net/problem/2749

import sys
input = sys.stdin.readline

n = int(input())

## N번째 피보나치 수를 M으로 나눈 나머지는 특정 주기를 가진다
## M = 10**k 일 때, 그 주기는 항상 `15 * 10**(k-1)` 이다
## 즉, M = 1000000 일 때, 주기는 `15 * M // 10` 이다

mod = 1000000  # 나눌 수
fibo = [0, 1]
p = 15 * mod // 10  # 피사노 주기

for i in range(2, p):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= mod

print(fibo[n % p])