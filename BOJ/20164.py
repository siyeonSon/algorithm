# 2023-08-20 21:29:56
# https://www.acmicpc.net/problem/20164

import sys
input = sys.stdin.readline

n = input().strip()

# 홀수 개수 찾기
def count_odd(n) :
    cnt = 0
    for char in n:
        if char in '13579':
            cnt += 1
    return cnt

answer = []
def odd_holic(n, cnt) :
    cnt += count_odd(n)
    
    len_n = len(n)
    if len_n == 1 :
        answer.append(cnt)
    elif len_n == 2 :
        odd_holic(str(int(n[0])+int(n[1])), cnt)
    else :
        for i in range(1, len_n) :
            for j in range(i+1, len_n) :
                odd_holic(str(int(n[:i]) + int(n[i:j]) + int(n[j:])), cnt)

odd_holic(n, 0)
print(min(answer), max(answer))