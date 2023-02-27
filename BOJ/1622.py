# 2023-02-27 15:11:27
# https://www.acmicpc.net/problem/1622

## sys.stdin.readline하면 출력 초과남
## 이유: https://www.acmicpc.net/board/view/112040#comment-176511

# 정답 1
while True :
    ans = ''
    try:
        a = sorted(input())
        b = sorted(input())
    except:
        break
    
    while a and b :
        if a[-1] == b[-1] :
            ans += a.pop()
            b.pop()
        elif a[-1] > b [-1] :
                a.pop()
        else :
             b.pop()

    print(''.join(sorted(ans)))

# 정답 2
try :
    while True :
        ans = []
        a = input()
        b = input()
        
        for s in a :
            if s in b :
                ans += [s]
                b = b.replace(s, '', 1)  # s를 ''으로 1개만 대체함
        ans.sort()
        print(''.join(ans))
except :
    pass