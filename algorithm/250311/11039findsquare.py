import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    rev_arr = list(map(list, zip(*arr)))
    answer = 0
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 1 :
                row_leng = 0
                col_leng = 0
                for o in arr[i][j:] :
                    if o == 1 :
                        row_leng += 1
                    else :
                        break
                for o in rev_arr[j][i:] :
                    if o == 1 :
                        col_leng += 1
                    else :
                        break
            else :
                continue
            if answer < (row_leng*col_leng) :
                answer = (row_leng*col_leng)
    print(f'#{tc} {answer}')
