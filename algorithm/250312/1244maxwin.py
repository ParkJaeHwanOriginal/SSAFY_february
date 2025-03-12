import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t+1) :
    num, cnt = input().split()
    lst = list(num)
    # print(lst)
    cnt = int(cnt)
    for i in range(cnt) :
        max_lst = sorted(num, reverse=True)
        # print(lst, max_lst)
        if max_lst == lst :
            if lst[0] != lst[1] :
                lst[-1], lst[-2] = lst[-2], lst[-1]
            continue

        max_target_idx = 0
        for l in range(len(lst)) :
            if lst[l] != max_lst[l] :
                max_target_idx = l
                break
        # print(max_target_idx)
        min_target_idx = len(lst) + 1
        max_target = 0
        for l in range(max_target_idx+1,len(lst)) :
            if lst[l] != max_lst[l] :
                if max_target < int(lst[l]) :
                    max_target = int(lst[l])
                    min_target_idx = l

        # print(min_target_idx)
        lst[max_target_idx], lst[min_target_idx] = lst[min_target_idx], lst[max_target_idx]
    print(f"#{tc} {''.join(lst)}")