# 2024-10-22 16:58:32
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key=lambda x: x[1])
    len_j = len(jobs)
    
    start = 0
    while len(jobs) > 0 :
        for i in range(len(jobs)) :
            if jobs[i][0] <= start :
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs) - 1:
                start += 1
    
    return answer // len_j