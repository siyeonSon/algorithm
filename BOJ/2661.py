# 2025-12-30 20:25:26
# https://www.acmicpc.net/problem/2661

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().strip())

# 마지막에 추가된 숫자를 기준으로 좋은 수열인지 확인하는 함수
# is_good() 함수의 한계: 궁극적으로 좋은 수열인지 확인하지는 못함
# 예: 123123213 은 좋은 수열이 아니지만 is_good()에서는 좋은 수열처럼 판단함
def is_good(nums) :
    ln = len(nums)
    for i in range(1, ln//2 + 1) :
        if nums[-i:] == nums[-i-i:-i] :  # index 뒤에서 계산하는 거 여전히 헷갈림
            return False
    return True

def backtrack(nums) :
    if len(nums) == n :
        print(nums)   # 처음 발견하는 nums가 최소인 좋은 수열임
        return True   # 답을 찾았음을 상위에 알림
    for i in ['1', '2', '3'] :
        if is_good(nums+i) :  # i를 추가한 숫자가 좋은 수열이라면
            if backtrack(nums+i) :
                return True  # 답을 찾았다면 즉시 리턴하여 재귀 종료
    return False

backtrack('')