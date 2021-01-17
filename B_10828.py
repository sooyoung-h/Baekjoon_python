import sys
n = int(sys.stdin.readline())
stk = []

def push(arr, item):
    arr.append(item)

def pop(arr):
    length = len(stk)
    if length == 0:
        print(-1)
    else:
        print(arr[length -1])
        del arr[length -1]
    
def size(arr):
    print(len(arr))
    
def empty(arr):
    if len(arr) == 0:
            print(1)
    else:
        print(0)
        
def top (arr):
    length = len(arr)
    if length == 0:
        print(-1)
    else:
        print(stk[length -1])

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(stk, command[1])
    elif command[0] == 'pop':
        pop(stk)
    elif command[0] == 'size':
        size(stk)
    elif command[0] == 'empty':
        empty(stk)
    elif command[0] == 'top':
        top(stk)
