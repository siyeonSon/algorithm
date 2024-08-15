# 2024-08-15 23:42:52
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# 정답
def solution(number, k) :
    answer = ''
    stack = []
    for n in number :
        # n이 더 클 경우 k-1 해주고 stack.pop() 함. k=0이 되면 stack에 넣어야 함
        while k > 0 and len(stack) > 0 and stack[-1] < n :
            k -= 1
            stack.pop()
        stack.append(n)
    
    answer = ''.join(stack[0:len(number)-k])
    return answer

# 오답 - 시간 초과 발생(100,000개에 대한 2중 for문) -> stack 사용
def find_idx(number, n, start, end) :
    for i in range(start, end) :
        if number[i] == n :
            return i

def solution(number, k):
    answer = []
    stack = []
    start = 0
    for end in range(k, len(number)) :
        MAX = max(number[start:end+1])
        start = find_idx(number, MAX, start, end+1) + 1
        answer.append(MAX)
    return "".join(answer)