def recur(cnt, i, j, result) :
    global path
    if path and result > min(path):
        return

    if cnt == (2*n)-1 :
        path.append(result)
        return

    cnt += 1
    if (i + 1) < n :
        next_result = result + arr[i+1][j]
        recur(cnt, i + 1, j, next_result)
    if (j + 1) < n :
        next_result = result + arr[i][j + 1]
        recur(cnt, i, j + 1, next_result)



t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]

    path = []
    recur(1, 0, 0, arr[0][0])
    print(f'#{tc} {min(path)}')
