# 2023-02-28 19:24:49
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import deque
from collections import defaultdict

def solution(tickets):
    answer = []
    tickets.sort(key = lambda x:(x[1], x[0]))
    
    dic = defaultdict(list)
    
    # 딕셔너리를 사용하여 중복 제거
    for [start, end] in tickets:
        dic[start].append(end)
    for k in dic.keys():
        dic[k].sort(reverse = True)
    
    def dfs():
        stack = ["ICN"]
        while stack:
            print(stack)
            start = stack[-1]
            if not dic[start]: # start에서 출발하는 항공편이 없는경우 바로 답에 넣기
                answer.append(stack.pop())
            else:
                stack.append(dic[start].pop())
    dfs()
    return answer[::-1]