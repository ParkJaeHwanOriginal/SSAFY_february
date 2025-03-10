t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]

    lst = [arr[0]]
    cnt = 0
    for i in arr[1:] :
        for ii in lst :
            if (i[0] > ii[0] and i[1] < ii[1]) or (i[0] < ii[0] and i[1] > ii[1]) :
                cnt += 1
        lst.append(i)

    print(f'#{tc} {cnt}')