# 2024-09-17 23:27:34
# https://www.acmicpc.net/problem/2852

import sys
input = sys.stdin.readline

n = int(input())
play = []
for _ in range(n) :
    team, time = list(input().split())
    time_sp = list(map(int, time.split(":")))
    play.append([int(team)-1, time_sp])
play.append(["END", [48, 00]])

score = [0, 0]
answer = [[0, 0], [0, 0]]
for i in range(len(play)) :
    team, time = play[i]
    if score[0] > score[1] :  # 1번 팀이 이기고 있던 상황
        pre_team, pre_time = play[i-1]
        answer[0][0] += time[0] - pre_time[0]
        answer[0][1] += time[1] - pre_time[1]
    elif score[0] < score[1] :  # 2번 팀이 이기고 있던 상황
        pre_team, pre_time = play[i-1]
        answer[1][0] += time[0] - pre_time[0]
        answer[1][1] += time[1] - pre_time[1]
    if team != "END" :
        score[team] += 1

# 시간 형식을 올바르게 변환하지 못해서 계속 틀림
def time_format(min, sec) :
    while True :
        if sec < 0 :
            min -= 1
            sec += 60
        elif sec > 60 :
            min += 1
            sec -= 60
        else :
            break

    min_s = str(min)
    sec_s = str(sec)
    if len(min_s) == 1 :
        min_s = "0" + min_s
    if len(sec_s) == 1 :
        sec_s = "0" + sec_s
    
    return min_s + ":" + sec_s

for a in answer :
    print(time_format(a[0], a[1]))