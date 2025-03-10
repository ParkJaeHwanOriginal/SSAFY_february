import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1) :
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    max_lst = 0
    for l in lst :
        if l > max_lst :
            max_lst = l
    cnt_lst = [0] * (max_lst+1)
    for l in lst :
        cnt_lst[l] += 1
    # print(cnt_lst)
    bung_lst = [0] * (max_lst+1)
    for l in range(m,(max_lst+1),m) :
        bung_lst[l] = k
    # print(bung_lst)

    temp_cus = 0
    temp_bung = 0
    for l in range(1, (max_lst+1)) :
        temp_cus += cnt_lst[l]
        temp_bung += bung_lst[l]
        if temp_cus > temp_bung :
            break
    if temp_cus > temp_bung or cnt_lst[0] != 0 :
        print(f'#{tc} Impossible')
    else :
        print(f'#{tc} Possible')