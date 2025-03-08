# 2025-03-07 16:32:41
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0 
    total = 0  # 다리 위에 놓인 무게
    
    # bridge의 길이를 유지하기 위해 0으로 채움. 시간이 지날 때마다 popleft
    bridge = deque([0] * bridge_length)
    trucks = deque([t for t in truck_weights])
    
    while trucks :
        curr_trk = bridge.popleft()
        total -= curr_trk
        if total + trucks[0] <= weight :
            next_trk = trucks.popleft()  # 다음 트럭
            bridge.append(next_trk)  # 이동
            total += next_trk
        else :
            bridge.append(0)
        answer += 1  # 시간 흐름
    answer += bridge_length  # 마지막 트럭이 다리를 지나는 시간
    return answer

## 문제 아이디어
# bridge의 길이를 유지하기 위해 0으로 채우는 것이 포인트
# 시간이 지나면 popleft() -> append() 하면서 0 또는 트럭을 채움