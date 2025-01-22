# 2024-11-03 01:11:51
# https://www.acmicpc.net/problem/3613

import sys
input = sys.stdin.readline

def cppToJava(str) :
    result = ''
    flag = False
    for s in str :
        if s.isupper() :
            return 'Error!'
        if s == '_' :
            if flag == True :
                return 'Error!'
            flag = True
            continue
        if flag :
            result += s.upper()
            flag = False
            continue
        result += s
    return result

def javaToCpp(str) :
    result = ''
    for s in str :
        if s.isupper() :
            result += '_' + s.lower()
            continue
        result += s
    return result

str = input().rstrip()

def isPossible(str) :
    if str[0].isupper() or not str[0].isalpha() or not str[-1].isalpha() or ' ' in str :
        return False
    return True

def solve(str) :
    if isPossible(str) :
        if '_' in str :
            return cppToJava(str)
        else :
            return javaToCpp(str)
    return 'Error!'

print(solve(str))