# 2023-03-20 19:51:02
# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    
    # rows X columns 행렬 생성
    nums = [i for i in range(1, rows*columns+1)]
    board = []
    for i in range(rows) :
        board.append(nums[columns*i:columns*i+columns])

    # 회전
    def rotate(x1, y1, x2, y2) :
        minimum = []
        # 사각형 상단 가로 줄
        pre = board[x1+1][y1]
        for i in range(y1, y2) :
            minimum.append(pre)
            ori = board[x1][i]
            board[x1][i] = pre
            pre = ori

        # 사각형 오른쪽 세로 줄
        for i in range(x1, x2) :
            minimum.append(pre)
            ori = board[i][y2]
            board[i][y2] = pre
            pre = ori

        # 사각형 하단 가로 줄
        for i in range(y2, y1, -1) :
            minimum.append(pre)
            ori = board[x2][i]
            board[x2][i] = pre
            pre = ori

        # 사각형 왼쪽 세로 줄
        for i in range(x2, x1, -1) :
            minimum.append(pre)
            ori = board[i][y1]
            board[i][y1] = pre
            pre = ori

        return min(minimum)

    for q in queries :
        answer.append(rotate(q[0]-1, q[1]-1, q[2]-1, q[3]-1))
    
    return answer