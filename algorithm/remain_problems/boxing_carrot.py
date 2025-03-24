t = int(input())
for tc in range(1, t+1) :
    n, m = map(int, input().split())
    arr = [ list(input().split()) for _ in range(n) ]
    answer = n * m
    for i in range(n-2) :
        for j in range(i+1, n-1) :
            cnt = 0
            for s in range(i+1) :
                cnt += arr[s].count("R")
                cnt += arr[s].count("B")
            for s in range(i+1, j+1) :
                cnt += arr[s].count("W")
                cnt += arr[s].count("B")
            for s in range(i+1, j+1) :
               	cnt += arr[s].count("W")
               	cnt += arr[s].count("R")
            if cnt < answer :
                answer = cnt
    print(f'#{tc} {answer}')

