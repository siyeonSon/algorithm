# 2026-01-28 21:23:14
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    # 알파벳 순서를 유지하기 위해 AEIOU -> 12345로 치환해서 생각함
    d = {'A': '1', 'E': '2', 'I': '3', 'O': '4', 'U': '5'}
    wm = [d[c] for c in word]
    
    w = []
    answer = 0
    while True :
        print(w)
        if w == wm :
            break
        if len(w) < 5 :
            w.append('1')
        else :
            # 길이가 5이고 마지막이 '5'('U')면, '5'가 아닌 숫자가 나올 때까지 pop
            while w[-1] == '5':
                w.pop()
            # 마지막 숫자를 다음 숫자로 증가시킴
            w[-1] = str(int(w[-1]) + 1)
        answer += 1

    return answer
