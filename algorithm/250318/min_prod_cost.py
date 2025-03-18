def combi(k, total = 0) :
    global answer
    if total > answer :
        return
    if k == n :
        if answer > total :
            answer = total
        return
    for i in range(n) :
        if visited[i] == 0 :
            visited[i] = 1
            combi(k+1, total + arr[k][i])
            visited[i] = 0

t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    rev_arr = list(map(list, zip(*arr)))
    answer = n*99
    visited = [0] * (n+1)
    combi(0)
    print(f'#{tc} {answer}')