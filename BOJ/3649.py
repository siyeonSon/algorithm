# 2026-01-11 16:39:04
# https://www.acmicpc.net/problem/3649

import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:  # EOF 체크: 읽어온 줄이 없으면 종료
        break

    try:
        x_cm = int(line)
        x_nm = x_cm * 10**7
        
        n_line = input().strip()
        if not n_line: break
        n = int(n_line)
        
        nums = []
        for _ in range(n):
            nums.append(int(input().strip()))

        nums.sort()

        answer = []
        le, ri = 0, n - 1
        
        while True:
            if le >= ri :
                break
            current_sum = nums[le] + nums[ri]
            
            if current_sum == x_nm:
                answer = [nums[le], nums[ri]]
                break  # 가장 차이가 큰 쌍을 찾으면 즉시 종료
            elif current_sum < x_nm:
                le += 1
            else:
                ri -= 1

        if answer:
            print("yes", *answer)
        else:
            print('danger')
            
    except EOFError:
        break
    except ValueError:
        break