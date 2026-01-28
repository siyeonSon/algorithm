# 2026-01-28 21:22:27
# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]
    
    def subpress(x, y, n) :  # 시작 위치: arr[x][y], 탐색 길이: n
        std = arr[x][y]
        for i in range(x, x+n) :
            for j in range(y, y+n) :
                if std != arr[i][j] :
                    n = n // 2
                    subpress(x, y, n)
                    subpress(x+n, y, n)
                    subpress(x, y+n, n)
                    subpress(x+n, y+n, n)
                    return
        answer[std] += 1

    subpress(0, 0, len(arr))
    return answer