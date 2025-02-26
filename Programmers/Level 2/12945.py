# 2025-02-24 21:02:51
# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    fibo = [0, 1]
    for i in range(n-1) :
        fibo.append((fibo[i+1] + fibo[i]) % 1234567)
    return fibo[-1]