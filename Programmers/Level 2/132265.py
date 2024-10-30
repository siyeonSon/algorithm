# 2024-10-30 18:52:02
# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    answer = 0
    big = Counter(topping)
    small = set()
    print(len(small))
    for t in topping :
        big[t] -=1
        small.add(t)

        if big[t] == 0 :
            big.pop(t)
        if len(big) == len(small) :
            answer += 1
    return answer