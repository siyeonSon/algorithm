# 2025-03-07 16:21:16
# https://school.programmers.co.kr/learn/courses/30/lessons/42860

# 참고한 코드
def solution(name):
    # 각 알파벳의 조이스틱 수 세기
    ordA = ord('A')
    ordZ = ord('Z')
    cnt = [min(ord(n) - ordA, ordZ - ord(n) + 1) for n in name]
    answer = sum(cnt)

    # 좌우 이동 최적화
    n = len(name)
    move = n - 1  # 오른쪽 끝까지 가는 경우

    for left in range(n):
        idx = left + 1
        while (idx < n) and (cnt[idx] == 0):
            idx += 1
        right = n - idx  # 반대 방향으로 이동하는 최소거리
        back_distance = min(left, right)        
        move = min(move, left + right + back_distance)
    answer += move
    return answer 

# 작성한 코드
def solution(name):
    # 각 알파벳의 조이스틱 수 세기
    ordA = ord('A')
    ordZ = ord('Z')
    move = [min(ord(n) - ordA, ordZ - ord(n) + 1) for n in name]
    answer = sum(move)

    # 좌우 이동 최적화
    length = len(name)
    min_move = length - 1  # 오른쪽 끝까지 가는 경우

    # 앞에서 부터 탐색
    for i in range(length):
        dup = 1
        # 연속된 'A' 건너뛰기
        while i+dup < length and name[i+dup] == 'A':
            dup += 1
        # i: 순방향 최소 거리, length-dup-i: 반대 방향으로 이동하는 최소거리
        back_distance = min(i, length-dup-i)
        # length-dup: 건너뛴 것을 제외하고 방문, 되돌아가는 거리
        min_move = min(min_move, length - dup + back_distance)
    answer += min_move
    return answer

## 테스트 케이스
# input: BBBAAAAAB, output: 8
# 뒤로 갔다가 앞으로 가는 케이스