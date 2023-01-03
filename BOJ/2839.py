# 2022-12-11 14:51:06
# https://www.acmicpc.net/problem/2839
# https://velog.io/@sians0209/boj2839

n = int(input())
result = []
for bag_5kg in range(n//5 + 1) :
    bag_3kg = (n - (bag_5kg * 5)) // 3
    if n - bag_5kg*5 - bag_3kg*3 == 0 :
        result.append(bag_5kg + bag_3kg)

if result : print(min(result))
else : print(-1)


# 2022-12-11 15:22:33
n = int(input())
result = 0
while n >= 0 :
    if n % 5 == 0 :
        result += n // 5
        print(result)
        break
    n -= 3
    result += 1
else : print(-1)