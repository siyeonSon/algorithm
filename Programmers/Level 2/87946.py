# 2025-02-24 21:47:38
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    
    def visit(k, path):
        count = 0
        for min_tired, minus_tired in path:
            if k < min_tired:
                break
            k -= minus_tired
            count += 1
        return count
    
    return max(visit(k, p) for p in permutations(dungeons))