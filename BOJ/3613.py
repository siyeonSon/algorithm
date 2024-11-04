# 2024-11-03 01:11:51
# https://www.acmicpc.net/problem/3613

import sys
input = sys.stdin.readline

def cppToJava(str) :
    result = ''
    flag = False
    for s in str :
        if flag :
            result += s.upper()
            flag = False
            continue
        if s == '_' :
            flag = True
            continue
        if s.isupper() :
            return 'Error!'
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

answer = ''
if '_' in str :
    answer = cppToJava(str)
else :
    answer = javaToCpp(str)
if str[0].isupper() :
    answer = 'Error!'
print(answer)