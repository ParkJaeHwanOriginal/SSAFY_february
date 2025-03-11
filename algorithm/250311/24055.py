import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    for l in range(n) :
        temp_lst = []
        temp_num = lst[l]
        for ll in lst[l:] :
            if temp_num < ll and ll not in temp_lst :
                temp_lst.append(ll)
                temp_num = ll
        if len(temp_lst) > answer :
            answer = len(temp_lst)
    print(f'#{tc} {answer}')
