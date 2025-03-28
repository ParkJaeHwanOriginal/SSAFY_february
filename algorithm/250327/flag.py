t = int(input())
for tc in range(1, t+1) :
    n, m = map(int, input().split())
    arr = [ list(input().split()) for _ in range(n) ]
    answer = n*m

    print(f'#{tc} {answer}')

