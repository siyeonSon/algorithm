# 2026-01-29 00:21:59
# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations

def solution(expression):    
    # 숫자와 연산자 분리하기
    nums, operations = [], []
    tmp = ''
    for e in expression :
        if e in '-*+' :  # 만약 부등호라면
            nums.append(int(tmp))
            operations.append(e)
            tmp = ''
        else :
            tmp += e
    nums.append(int(tmp))
    
    print(nums, operations)
    
    answer = 0
    for order in permutations(set(operations)) :
        print(order)
        answer = max(answer, calculate_by_order(nums, operations, order))
    return answer

"""
연산자 우선순위에 따라 연산을 처리하여 최종 값을 반환하는 함수

Args:
    nums(list): 숫자
    operations(list): 연산자
    order(tuple): 연산자 우선순위

Returns:
    int: 연산의 결과(절대값)
"""
def calculate_by_order(nums, operations, order) :
    nums = nums[:]
    operations = operations[:]
    for target in order :
        i = 0
        while target in operations :   # 해당 연산자를 모두 제거할 때까지
            if operations[i] == target :
                nums[i] = calculate(nums[i], target, nums[i+1])
                nums.pop(i+1)
                operations.pop(i)
            else :
                i += 1
    return abs(nums[0])
        
"""
+, -, * 분기처리로 계산을 처리하는 함수
"""

def calculate(num1, operation, num2) :
    if operation == '+' :
        return num1 + num2
    elif operation == '-' :
        return num1 - num2
    elif operation == '*' :
        return num1 * num2