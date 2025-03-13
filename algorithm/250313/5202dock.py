import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    lst = []
    for i in range(n) :
        s, e = map(int, input().split())
        lst.append([(e-s+1), s, e])

    lst.sort()
    cnt = 0
    time_lst = [0] * 25
    # print(lst)
    for i in lst :
        # print(i[1], i[2])
        if sum(time_lst[i[1]:i[2]]) == 0:
            for ii in range(i[1],i[2]) :
                time_lst[ii] = 1
            cnt += 1
    print(f'#{tc} {cnt}')
