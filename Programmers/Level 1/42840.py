def solution(answers):
    answer = []
    problems = [[1, 2, 3, 4, 5], 
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    len_p = [5, 8, 10]
    len_a = len(answers)

    # 채점
    scores = [0, 0, 0]
    for i in range(len_a) :
        for j in range(3) :
            if answers[i] == problems[j][i%len_p[j]] :
                scores[j] += 1
    
    # 점수 계산
    max_s = max(scores)
    for i in range(3) :
        if scores[i] == max(scores) :
            answer.append(i+1)
    return answer