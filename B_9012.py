import sys
n = int(sys.stdin.readline().rstrip())

line = [0] * n
result = [0] * n

for i in range(n):
    left = 0
    line[i] = sys.stdin.readline().rstrip()

    for q in line[i]:
        if left < 0:
            result[i] = 'NO'
            break
        elif q == ')':
            left -= 1
        elif q == '(':
            left += 1

    if result[i] != 'NO':
        if left == 0:
            result[i] = 'YES'
        else:
            result[i] = 'NO'

for j in range(n):
    print(result[j])
