n = int(input()) # 총 수열의 개수
stack = []
result = []
count = 1
ok = True

for i in range(n):
    num = int(input())      
    while count <= num:     #같아질 때까지 push
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == num:    #같으면 pop
        stack.pop()
        result.append('-')
    else:
        ok = False

if ok == False:
    print('NO')
else:
    for k in result:
        print(k)
