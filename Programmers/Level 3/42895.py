# 2025-03-04 00:05:48
# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    if N == number :
        return 1
    # dp[i]는 N을 i번 사용해서 만들 수 있는 모든 수의 집합
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    
    for i in range(2, 9) :
        # N을 i번 연속해서 사용하는 경우 (예: 5, 55, 555, ...)
        dp[i].add(int(str(N)*i))
        
        # 사칙연산
        for j in range(1, i) :
            for x in dp[j] :  # j번 사용한 수
                for y in dp[i-j] :  # i-j번 사용한 수
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0 :
                        dp[i].add(x // y)
            if number in dp[i] :
                return i
    return -1