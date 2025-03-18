def combi(k, total = 1) :
    global answer
    # if total < answer :
    #     return
    if k == n :
        if answer < total :
            answer = total
        return
    for i in range(n) :
        if visited[i] == 0 :
            if total * (arr[k][i]/100) <= answer :
                continue
            visited[i] = 1
            combi(k+1, total * (arr[k][i]/100))
            visited[i] = 0

t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    answer = 0
    visited = [0] * (n+1)
    combi(0)
    print(f'#{tc} {answer*100:.6f}')
