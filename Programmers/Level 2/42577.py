# 2024-05-07 12:30:11
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    spb = sorted(phone_book)
    for i in range(len(spb)-1) :
        if spb[i+1].startswith(spb[i]) :
            return False
    return True