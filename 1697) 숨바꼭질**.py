# 파이썬은 리스트를 queue처럼 사용할 수 있으나
# pop(0)은 O(n)으로 너무 느리다 
# -> collections의 deque 사용! O(n)으로 해결

import sys
from collections import deque

LIMIT = 100001

def solve(arr, n, k):
    q = deque()
    q.append(n) #잡는 사람의 현위치
    
    while q:
        i = q.popleft() # i : 바뀐 위치

        if i == k: #바뀐 위치가 도착한 거면 움직인 횟수 반환!
            return arr[i]

        for j in (i+1, i-1, 2*i):
            #안에 들어오면 저장
            if (0 <= j < LIMIT) and arr[j] == 0:
                arr[j] = arr[i] + 1 # 움직인 횟수 더해주기
                q.append(j) # 움직이는 위치 저장

N, K = map(int, sys.stdin.readline().split())
find = [0] * LIMIT
print(solve(find,N,K))
