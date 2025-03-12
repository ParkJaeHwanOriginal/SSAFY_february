card = ['A', 'J', 'Q', 'K']
path = []
result = 0

def cnt_3() :
    cnt = 0
    lst_i = ''
    for i in path :
        if not lst_i :
            lst_i = i
            cnt += 1
            continue
        if i == lst_i :
            cnt += 1
        else :
            cnt = 0
        if cnt == 3 :
            return True

def recur(cnt) :
    global result
    if cnt == 5 :
        if cnt_3() :
            result += 1
            print(path)
        return

    for idx in range(4) :
        path.append(card[idx])
        recur(cnt + 1)
        path.pop()

recur(0)