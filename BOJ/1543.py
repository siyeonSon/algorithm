# 2023-11-25 11:09:30
# https://www.acmicpc.net/problem/1543

import sys
input = sys.stdin.readline

## 방법 1
print(input().rstrip().count(input().rstrip()))


## 방법 2
document = input().rstrip()
word = input().rstrip()
answer = 0

while (len(document) >= len(word)):
    snip = document[0:len(word)]
    if (snip == word):
        answer += 1
        document = document[len(word):]
    else:
        document = document[1:]

print(answer)