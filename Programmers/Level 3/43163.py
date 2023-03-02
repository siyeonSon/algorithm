from collections import deque

def solution(begin, target, words):
    if target not in words :
        return 0
    
    queue = deque()
    queue.append([begin, 0])
    
    while queue :
        word, answer = queue.popleft()    
        if word == target :
            return answer
        
        for i in range(len(words)) :
            if exchangable(word, words[i]) :
                queue.append([words[i], answer+1])
    
    return 0  # target 값은 있지만 만들 수 없을 때


# 두 단어가 서로 변환 가능한 관계일 때
def exchangable(w1, w2) :
    #두 단어의 길이가 다른 경우 False 반환
    if len(w1) != len(w2) :
        return False
    
    # 차이가 1인 경우에 True 반환
    cnt = 0
    for i in range(len(w1)) :
        if w1[i] != w2[i] :
            cnt += 1
    if cnt == 1 :
        return True
    return False