def tohex(n) :
    num = 0
    num_dict = { 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15 }
    for l in range(len(n)) :
        if n[l].isdigit() :
            num += int(n[l]) * (16**(len(n)-l-1))
        else :
            num += num_dict[n[l]] * (16**(len(n)-l-1))
    return num

t = int(input())
for tc in range(1, t+1) :
    n, k = map(int, input().split())
    rot = n//4
    arr = input()
    # print(arr)
    num_lst = []
    for l in range(rot) :
        temp_lst = arr[l:] + arr[:l]
        # print(temp_lst)
        for ll in range(4) :
            num16 = temp_lst[ll*rot:(ll+1)*rot]
            num_lst.append(num16)
    num_lst = set(num_lst)
    print(num_lst)
    answer_lst = []
    for l in num_lst :
        # print(tohex(l))
        answer_lst.append(tohex(l))
    answer_lst = sorted(answer_lst,reverse=True)
    print(answer_lst)
    print(f'#{tc} {sorted(answer_lst, reverse=True)[k-1]}')
