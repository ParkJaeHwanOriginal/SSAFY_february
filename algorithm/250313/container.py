t = int(input())
for tc in range(1, t+1) :
    n, m = map(int,input().split())
    con_lst = list(map(int, input().split()))
    truck_lst = list(map(int, input().split()))
    for i in range(0, len(con_lst)-1) :
        for ii in range(i, len(con_lst)) :
            if con_lst[i] < con_lst[ii] :
                con_lst[i], con_lst[ii] = con_lst[ii], con_lst[i]
    for i in range(0, len(truck_lst)-1) :
        for ii in range(i, len(truck_lst)) :
            if truck_lst[i] < truck_lst[ii] :
                truck_lst[i], truck_lst[ii] = truck_lst[ii], truck_lst[i]
    # con_lst.sort(reverse = True)
    # truck_lst.sort(reverse = True)
    sum = 0
    truck_ok = [False] * m
    truck_idx = 0
    for i in con_lst :
        if i <= truck_lst[truck_idx] :
            sum += i
            truck_idx += 1
        if truck_idx == m :
            break
    print(f'#{tc} {sum}')