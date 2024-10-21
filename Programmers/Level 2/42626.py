# 2024-10-21 14:26:33
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    mn = heapq.heappop(scoville)
    while mn < K:
        try:
            new = mn + (heapq.heappop(scoville) * 2)
        except:
            return -1
        heapq.heappush(scoville, new)
        mn = heapq.heappop(scoville)
        answer += 1

    return answer