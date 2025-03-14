import sys
sys.stdin = open('input.txt', 'r')

def dfs(k, i, j, lst) :
    if k == 7 :
        answer_lst.append(lst)
        return

    for l in rdlu :
        ni = i + l[0]
        nj = j + l[1]
        if 0 <= ni < 4 and 0 <= nj < 4 :
            dfs(k+1, ni, nj, (lst*10) + arr[ni][nj])



t = int(input())
for tc in range(1, t+1) :
    arr = [ list(map(int, input().split())) for _ in range(4) ]
    rdlu = [[0,1],[1,0],[0,-1],[-1,0]]

    answer_lst = []
    for i in range(4) :
        for j in range(4) :
            dfs(1, i, j, arr[i][j])

    print(f'#{tc} {len(set(answer_lst))}')