# 2023-02-22 14:03:59
# https://www.acmicpc.net/problem/1138

import sys
input = sys.stdin.readline

n = int(input())
location = list(map(int, input().split()))

ans = [0] * n
ans[location[0]] = 1  # 1의 위치

def find_index(i) :
    cnt = 0
    for j in range(n) :
        if ans[j] == 0 :
            if cnt == location[i] :
                ans[j] = i+1
            cnt += 1

for i in range(1, n) :
    find_index(i)

print(*ans)


# 2023-02-24 14:12:43
# https://www.acmicpc.net/problem/1138_2

import sys
input = sys.stdin.readline

n = int(input())
think = list(map(int, input().split()))
ans = [0] * n

for i in range(n) :
    cnt = 0
    for j in range(n) :
        if ans[j] == 0 :  # 아직 방문하지 않은 노드
            if cnt == think[i] :
                ans[j] = i+1
                break
            cnt += 1
print(*ans)