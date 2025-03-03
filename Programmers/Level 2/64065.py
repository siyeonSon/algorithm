# 2025-03-03 20:47:27
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    n_tuple = sorted(make_tuples(s), key=len)
    for tuple in n_tuple :
        for t in tuple :
            if t not in answer :
                answer.append(t)
    return answer

# 튜플 생성한다
def make_tuples(s) :
    result = []
    for str in s.split("},") :
        tuple = []
        num = ""
        for s in str :
            if s.isdigit() :
                num += s
            elif num :
                tuple.append(int(num))
                num = ""
        if num :
            tuple.append(int(num))
        result.append(tuple)
    return result