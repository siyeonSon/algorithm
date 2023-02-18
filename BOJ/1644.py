# 2023-02-18 15:25:40
# https://www.acmicpc.net/problem/1644

import sys
input = sys.stdin.readline

def eratos(n):
    sieve = [True] * (n+1)
    for i in range(2, int((n+1)**0.5) + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

ans = 0
left, right = 0, 0

n = int(input())
nums = eratos(n)  # 소수

if n in nums :
    ans = 1

while True :
    SUM = sum(nums[left:right])
    if n == 1 :
        break
    if left == len(nums)-1 :   # 끝지점에 도달했을 때
        break
    if SUM < n :
        right += 1
    elif SUM > n :
        left += 1
    else :
        ans += 1
        right += 1

print(ans)