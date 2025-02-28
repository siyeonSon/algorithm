# 2025-02-28 19:44:14
# https://www.acmicpc.net/problem/12015

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

LIS = [0]
for num in nums :
    if LIS[-1] < num :  # 최대값인 경우 길이를 늘림
        LIS.append(num)
    else :  # 이분 탐색
        left, right = 0, len(LIS)
        while left < right :
            mid = (left + right) // 2
            if LIS[mid] < num :
                left = mid + 1
            else :
                right = mid
        LIS[right] = num
print(len(LIS)-1)

### 참고
# 기존 값을 대체하면 LIS의 길이를 유지하면서 최적의 상태를 유지할 수 있음
# DP + 이분 탐색은 LIS의 실제 수열을 구하는 것이 아닌 길이만 구하는 방법임