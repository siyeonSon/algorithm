# 2023-02-24 14:30:54
# https://www.acmicpc.net/problem/1254

import sys
input = sys.stdin.readline

# 홀수인 경우
def case1(str) :
    mid = len(str) // 2
    for i in range(mid) :
        if str[mid-i] != str[mid+i] :
            return False
    return True

# 짝수인 경우
def case0(str) :
    mid = len(str) // 2
    end = len(str) - 1
    for i in range(mid) :
        if str[i] != str[end-i] :
            return False
    return True

# palindrome인 경우 True 반환
def palindrome(str) :
    if len(str) % 2 == 0 :
        return case0(str)
    else :
        return case1(str)

s = input().strip()
ans = len(s)
if palindrome(s) :
    print(ans)
else :
    for i in range(len(s)+1) :
        str = s + s[i::-1]
        if palindrome(str) :
            break
    print(ans + i + 1)