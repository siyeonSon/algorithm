# 2024-05-07 12:30:11
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    s_phone_book = sorted(phone_book)
    for i in range(len(s_phone_book)-1) :
        l = len(s_phone_book[i])
        if s_phone_book[i] in s_phone_book[i+1][:l] :
            return False
    return True