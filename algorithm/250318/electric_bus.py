t = int(input())
for tc in range(1, t+1) :
    n, *lst = map(int, input().split())
    at = 0
    answer = 0
    while at != n-1 :
        go = lst[at]
        if at + go >= n-1 :
            break
        fuel_lst = lst[at+1:at+go+1]
        max_leng = 0
        idx = 0
        dis_leng = -1
        for i in range(len(fuel_lst), 0, -1) :
            dis_leng += 1
            if fuel_lst[i-1] - dis_leng > max_leng :
                max_leng = fuel_lst[i-1]
                idx = i
        go = fuel_lst[idx-1]
        at += idx
        answer += 1
    print(f'#{tc} {answer}')
