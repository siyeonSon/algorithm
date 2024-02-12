# 2024-02-12 18:48:33
# https://www.acmicpc.net/problem/1802

import sys
input = sys.stdin.readline

n = int(input())

def is_palindrome(str) :
    if len(str) == 1:
        return True
    mid = len(str)//2
    for i in range(mid) :
        if str[i] == str[-i-1] :
            return False
    return is_palindrome(str[:mid])  # 반을 잘랐을 때도 회문인지 검증

for _ in range(n) :
    str = list(map(int, input().strip()))
    if is_palindrome(str) :
        print("YES")
    else :
        print("NO")