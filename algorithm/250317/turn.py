t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    arr = [ list(input().split()) for _ in range(n) ]
    lst = [''] * n
    print(f'#{tc}')
    for l in range(n) :
        for i in range(n-1, -1, -1) :
            lst[l] += arr[i][l]
        lst[l] += ' '
        for i in range(n-1, -1, -1) :
            lst[l] += arr[n-(l+1)][i]
        lst[l] += ' '
        for i in range(n) :
            lst[l] += arr[i][n-(l+1)]
        print(lst[l])