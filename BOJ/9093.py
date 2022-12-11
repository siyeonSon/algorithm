# 2022-12-10 20:32:40
# https://www.acmicpc.net/problem/9093
n = int(input())
for _ in range(n) :
    result = []
    str = input().split(" ")
    for s in str :
        result.append("".join(reversed(s)))
    print(" ".join(result))