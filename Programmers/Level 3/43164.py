# 2023-02-28 19:24:49
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

'''
틀린 이유
ICN -> A, A -> B, ICN -> C, C -> ICN 의 경우
나의 풀이: ICN -> A -> B
정답: ICN -> C -> ICN -> A -> B

나의 풀이로는 모든 티켓을 사용할 수 없다.
해결: 도착지로부터 출발 티켓이 없는 티켓을 나중에 사용해야 한다.
'''

import sys
sys.setrecursionlimit(10**6)
answer = ['ICN']

def solution(tickets):
    global answer
    tickets.sort(key = lambda x: (x[0], x[1]))
    used = [False] * len(tickets)
    print(tickets)
    
    # "ICN" 공항에서 출발
    dfs('ICN', tickets, used)
    
    return answer

def dfs(city, tickets, used) :
    global answer
    for i in range(len(tickets)) :
        if tickets[i][0] == city and not used[i] :
            if tickets[i][1] : 
                used[i] = True  # 티켓 사용
                answer.append(tickets[i][1])  # 도착지 저장
                dfs(tickets[i][1], tickets, used)  # 도착지를 출발지로 하는 티켓 탐색