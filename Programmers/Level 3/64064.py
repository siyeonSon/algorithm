# 2024-03-21 18:09:36
# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations

def correct(user, banned) :
        if len(user) != len(banned) :
            return False
        for i in range(len(user)) :
            if banned[i] == "*" :
                continue
            if user[i] != banned[i] :
                return False
        return True

def solution(user_id, banned_id):
    answer = 0
    suspect = []
    b = len(banned_id)
    for perm in permutations(user_id, b) : 
        match = True
        for i in range(b) : 
            if not correct(perm[i], banned_id[i]) : 
                match = False
        if match :
            if set(perm) not in suspect : 
                suspect.append(set(perm))
    answer = len(suspect)
    return answer