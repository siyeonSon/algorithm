# 2025-12-29 23:45:00
# https://www.acmicpc.net/problem/5052

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t) :
    n = int(input().rstrip())
    nums = []
    for _ in range(n) :
        nums.append(input().rstrip())

    nums.sort()
    # 사전순으로 정렬하면 접두어 관계에 있는 두 번호는 반드시 서로 인접함

    def solve(n, nums) :
        for i in range(n-1) :
                if nums[i+1].startswith(nums[i]):
                    return 'NO'
        return 'YES'

    print(solve(n, nums))

## Trie 자료구조로도 해결할 수 있음
'''
전화번호 911, 976, 9112를 순서대로 넣는다고 가정할 때

1) 911 삽입: 정상 삽입, 마지막 1 노드에 is_end = True 표시
2) 976 삽입: 정상 삽입
3) 9112 삽입: 9 -> 1 -> 1까지 내려갔을 때, 이미 is_end가 True인 지점을 만남 => NO 반환
'''
class Node:
    def __init__(self):
        self.child = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, number):
        curr = self.root
        for char in number:
            # 번호를 삽입하는 도중 이미 is_end가 True인 노드를 만난 경우 (기존 번호가 내 번호의 접두어임)
            if curr.is_end:
                return False
            
            if char not in curr.child:
                curr.child[char] = Node()
            curr = curr.child[char]
        
        # 번호 삽입을 마쳤는데, 해당 노드에 이미 자식 노드(child)가 존재하는 경우 (내 번호가 기존 번호의 접두어임)
        if curr.child:
            return False
            
        curr.is_end = True
        return True

trie = Trie()
is_consistent = True
for num in nums:
    if not trie.insert(num):
        is_consistent = False
        break