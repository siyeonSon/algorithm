# 2024-02-19 16:20:55
# https://www.acmicpc.net/problem/12018

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def listen(p_list, l) :
    dif = len(p_list) - l
    if dif < 0 :
        return 1
    elif dif == 0 :
        return min(p_list)
    p_list.remove(min(p_list))
    return listen(p_list, l)

def register(m_list, m, cnt) :
    if len(m_list) < 1 or m - m_list[0] < 0 :
        return cnt
    return register(m_list[1:], m - m_list[0], cnt + 1)

m_list = []
for _ in range(n) :
    p, l = map(int, input().split())
    p_list = list(map(int, input().split()))
    m_list.append(listen(p_list, l))

print(register(sorted(m_list), m, 0))