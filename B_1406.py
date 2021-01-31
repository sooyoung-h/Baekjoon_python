# O(n)으로 시간초과...배열 추가,삭제할때마다 O(n)이라서 
import sys
data = list(sys.stdin.readline().strip())
n = int(input())
cursor = len(data)

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command[0] == 'P':
        data.insert(cursor, command[2]) #O(n)
        cursor += 1
    elif command[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor != len(data):
            cursor += 1
    elif command[0] == 'B':
        if cursor != 0:
            del s[cursur-1] #O(n)
            cursor -= 1
    
print("".join(data))
