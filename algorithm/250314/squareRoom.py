import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    rdlu = [[0,1],[1,0],[0,-1],[-1,0]]
    go = [0] * (n**2+1)
    for i in range(n) :
        for j in range(n) :
            num = arr[i][j]
            for l in rdlu :
                ni = i + l[0]
                nj = j + l[1]
                if 0 <= ni < n and 0 <= nj < n :
                    if (num + 1) == arr[ni][nj] :
                        go[num] = num
                        break
    # print(go) # 뒤집었을때도 해야하는듯
    max_leng = 0
    temp_leng = 1
    for i in range(1, len(go)) :
        if go[i-1] == 0 :
            temp_leng = 1
        elif go[i-1] == go[i] - 1 :
            temp_leng += 1
        elif go[i] == 0 :
            if max_leng < temp_leng :
                max_leng = temp_leng
        if max_leng < temp_leng:
            max_leng = temp_leng
    # print(max_leng)

    min_num = 0
    temp_leng = 0
    for i in range(1, len(go)) :
        if go[i] != 0 :
            temp_leng += 1
            if go[i-1] == 0 :
                min_num = go[i]
        else :
            if temp_leng == max_leng :
                break
            else :
                temp_leng = 0
    print(f'#{tc} {min_num} {max_leng+1}')

