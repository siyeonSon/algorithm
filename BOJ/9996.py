# 2024-08-30 00:11:56
# https://www.acmicpc.net/problem/9996

import sys
input = sys.stdin.readline

def matchStart(pattern, file) :
    for i in range(len(pattern)) :
        if pattern[i] != file[i] :
            return False
    return True

def matchEnd(pattern, file) :
    for i in range(1, len(pattern)+1) :
        if pattern[-i] != file[-i] :
            return False
    return True

def solve(pattern, file) :
    splitted_pat = pattern.split('*')
    if len(splitted_pat) == 1 :
        return matchStart(pattern, file)
    elif len(splitted_pat) == 2 :
        if len(splitted_pat[0]) + len(splitted_pat[1]) > len(file) :
            return False
        return matchStart(splitted_pat[0], file) and matchEnd(splitted_pat[1], file)

n = int(input())
pattern = input().strip()
for _ in range(n) :
    file = input().strip()
    print("DA" if solve(pattern, file) else "NE")