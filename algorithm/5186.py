import sys
sys.stdin = open("input.txt", "r")

tc = int(input())
for i in range(1, tc+1) :
    n = float(input())
    cnt = 0
    answer = ''
    while cnt < 13:
        cnt += 1
        num = 2 ** (0-cnt)
        if n >= num :
            n -= num
            answer += '1'
        else :
            answer += '0'
        if n == 0 :
            break
    if len(answer) == 13 :
        print(f'#{i} overflow')
    else :
        print(f'#{i} {answer}')
