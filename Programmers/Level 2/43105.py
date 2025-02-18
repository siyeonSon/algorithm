def solution(triangle):
    rev = triangle[::-1]
    
    for i in range(len(rev)-1) :
        for j in range(len(rev[i+1])) :
            rev[i+1][j] += max(rev[i][j], rev[i][j+1])
    
    return rev[-1][0]