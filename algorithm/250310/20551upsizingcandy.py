import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1) :
    a, b, c = map(int, input().split())
    if b < 2 or c < 3 :
        print(f'#{tc} -1')
        continue
    eat_count = 0
    if b >= c :
        eat_count += b-c+1
        b = c-1
    if a >= b :
        eat_count += a-b+1

    print(f'#{tc} {eat_count}')