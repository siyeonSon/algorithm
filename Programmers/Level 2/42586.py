# 2025-02-26 18:54:02
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)) :
        queue.append(math.ceil((100-progresses[i])/speeds[i]))
    
    while queue :
        cnt = 1
        date = queue.popleft()
        # 뒤에 있는 기능과 함께 배포
        while queue :
            if date < queue[0] :
                break
            queue.popleft()
            cnt += 1
        answer.append(cnt)
    return answer