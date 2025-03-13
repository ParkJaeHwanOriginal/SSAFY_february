import sys
sys.stdin = open("input.txt", "r")

def check(lst) :
    count_lst = [0] * 10
    win = False
    for i in lst :
        count_lst[i] += 1
    for i in range(0, 8) :
        if count_lst[i] >= 1 and count_lst[i+1] >= 1 and count_lst[i+2] >= 1 :
            win = True
    for i in count_lst :
        if i == 3 :
            win = True
    return win

t = int(input())
for tc in range(1, t+1) :
    lst = list(map(int, input().split()))
    player = [[],[]]
    for i in range(len(lst)) :
        if i % 2 == 0 :
            player[0].append(lst[i])
        else :
            player[1].append(lst[i])

    for i in range(3, 6 + 1) :
        win_player = 0
        for l in range(2) :
            check_lst = player[l][:i]
            if check(check_lst) :
                win_player = l+1
                break
        if win_player != 0 :
            break

    print(f'#{tc} {win_player}')


