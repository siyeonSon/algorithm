# 2024-10-14 15:49:25
# https://www.acmicpc.net/problem/2529

import sys
input = sys.stdin.readline

# 부등호가 올바른지 확인
def check(n1, n2, simbol) :
    if simbol == ">" :
        return n1 > n2
    else :
        return n1 < n2

def backTracking(idx, word) :
    global mx, mn

    # idx가 부등호 문자의 개수보다 크다면 모든 숫자를 알맞게 넣은 것
    if idx > k :
        # 맨처음 만족하는 값이 최소, 마지막에 저장되는 것이 최대
        if mn == "" :
            mn = word
        else :
            mx = word
        return
    
    for i in range(10) :
        if not visited[i] :
            if idx == 0 or check(word[-1], str(i), m[idx-1]) :
                visited[i] = True
                backTracking(idx+1, word + str(i))
                visited[i] = False

k = int(input())
m = list(input().split())
visited = [False] * 10
mx, mn = "", ""
backTracking(0, "")

print(mx)
print(mn)