# 2025-02-24 20:06:03
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    r = len(arr1[0])
    answer = [[0] * m for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            for k in range(r) :
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer