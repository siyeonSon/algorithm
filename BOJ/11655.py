# 2024-08-27 11:34:57
# https://www.acmicpc.net/problem/11655

import sys

string = input()

answer = ""
ascii_a, ascii_z = ord("a"), ord("z")  # 65, 90
ascii_A, ascii_Z = ord("A"), ord("Z")  # 97, 122
alp_len = ascii_z - ascii_a + 1

def isAlpabetRange(num) :
    return ascii_a <= num <= ascii_z or ascii_A <= num <= ascii_Z

def isLowerAlpabetRange(num) :
    return ascii_a <= num <= ascii_z

def isUpperAlpabetRange(num) :
    return ascii_A <= num <= ascii_Z

for str in string :
    ascii_str = ord(str)
    if not isAlpabetRange(ascii_str) :  # 알파벳이 아닌 경우
        answer += str
        continue
    
    enc = ascii_str + 13
    if isLowerAlpabetRange(ascii_str) :  # 소문자인 경우
        if isLowerAlpabetRange(enc) :  # 암호화도 소문자
            answer += chr(enc)
        else :  # 암호화는 소문자가 아님
            answer += chr(enc - alp_len)
    
    if isUpperAlpabetRange(ascii_str) :  # 대문자인 경우
        if isUpperAlpabetRange(enc) :  # 암호화도 대문자
            answer += chr(enc)
        else :  # 암호화는 대문자가 아님
            answer += chr(enc - alp_len)

print(answer)