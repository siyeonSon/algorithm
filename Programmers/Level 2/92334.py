# 2025-02-26 19:17:57
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    # 신고 회수 세기
    report_dic = dict()
    for r in report :
        reporter, reportee = r.split(" ")
        if reportee in report_dic :
            report_dic[reportee].add(reporter)
        else :
            report_dic[reportee] = set([reporter])

    # 메일 회수 세기
    id_dic = dict()
    for id in id_list :
        id_dic[id] = 0
        
    for key, value in report_dic.items() :
        if len(value) >= k :
            for id in value :
                id_dic[id] += 1
    
    return [cnt for id, cnt in id_dic.items()]