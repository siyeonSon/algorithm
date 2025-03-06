# 2025-03-06 20:45:31
# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    n = len(money)
    
    # 첫번째 집을 방문 O, 마지막 원소 탐색 X
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])  # dp1[1] 초기화 필요: 테스트 케이스 [5,1,2]
    for i in range(2, n-1): 
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    # 첫번째 집을 방문 X, 마지막 원소 탐색 O
    dp2 = [0] * n
    dp2[0] = 0  
    dp2[1] = money[1]
    for i in range(2, n): 
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    return max(dp1[-2], dp2[-1])

## 어려웠던 점
# dp1[1] 초기화를 고려하지 못했음
# 테스트 케이스 input: [5,1,2], answer: 5