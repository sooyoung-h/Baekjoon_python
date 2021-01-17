import sys
n = int(sys.stdin.readline().rstrip())
s = [0]*n # 문자열 저장
col = [0]*n #단어 개수 저장

i = 0
while i < n:
    s[i] = sys.stdin.readline().split()
    col[i] = len(s[i])
    j=0
    while j < col[i]:
       print(s[i][j][::-1], end=" ")
       j+=1
    i+=1

#문자열을 2차원배열로 저장
