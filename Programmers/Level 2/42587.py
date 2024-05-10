# 2024-05-10 19:21:06
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):  # 우선 순위가 더 큰 게 있다면
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer