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

#(정답)
# 스택 두개를 만들어서 커서 이동할 때 마다 양쪽 스택에서 이동시킴 -> O(1)
import sys
data1 = list(sys.stdin.readline().strip())
data2 = []
n = int(input())
cursor = len(data1)

for i in range(n):
    command = sys.stdin.readline().strip()
    if command[0] == 'P':
        data1.append(command[2]) #stdin 입력은 띄어쓰기 포함하니까 
    elif command[0] == 'L' and data1 != []:
        data2.append(data1.pop())
    elif command[0] == 'D' and data2 != []:
        data1.append(data2.pop())
    elif command[0] == 'B' and data1 != []:
        data1.pop()
print("".join(data1 + list(reversed(data2))))
        
