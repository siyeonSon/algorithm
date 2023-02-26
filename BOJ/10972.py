# 2023-02-26 21:55:57
# https://www.acmicpc.net/problem/10972
# https://velog.io/@sians0209/boj10972

import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

for i in range(n-1, 0, -1) :
    if m[i-1] < m[i] : # 앞 < 뒤
        for j in range(n-1, 0, -1) :
            if m[i-1] < m[j] :
                m[i-1], m[j] = m[j], m[i-1]
                m = m[:i] + sorted(m[i:])
                print(*m)
                exit()  # 코드 종료

print(-1)  # 코드 종료 발생 X -> -1 출력