# 2024-03-21 19:09:03
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil

def calculate_time(in_time, out_time) :
    in_hour, in_min = map(int, in_time.split(":"))
    out_hour, out_min = map(int, out_time.split(":"))
    return (out_hour - in_hour) * 60 + out_min - in_min
    
def calculate_fee(fees, time) :
    base_time, base_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    if time <= base_time :
        return base_fee
    return base_fee + ceil((time-base_time)/unit_time) * unit_fee

def solution(fees, records):
    answer = []
    car_times = {}
    n = len(records)
    for i in range(n) :
        time, car, type = records[i].split()
        if car not in car_times :  # 딕셔너리 초기화
            car_times[car] = 0
        if type == "IN" :
            out_flag = False
            for j in range(i+1, n) :  # 출차 기록을 찾음
                n_time, n_car, n_type = records[j].split()
                if n_car == car and n_type == "OUT" :
                    car_times[car] += calculate_time(time, n_time)
                    out_flag = True
                    break
            if not out_flag :  # 출차 기록이 없는 경우
                car_times[car] += calculate_time(time, "23:59")
    
    # 차량 번호 순서대로 정렬
    for k in sorted(car_times.keys()) :
        answer.append(calculate_fee(fees, car_times[k]))
    return answer