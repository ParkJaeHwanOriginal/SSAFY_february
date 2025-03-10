t = int(input())
for tc in range(1, t+1) :
    n, m, r, c, l = map(int, input().split())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    # print(arr)

    rdlu = [[0,1],[1,0],[0,-1],[-1,0]]
    pipe_rdlu = { 1 : [1,1,1,1],
                  2 : [0,1,0,1],
                  3 : [1,0,1,0],
                  4 : [1,0,0,1],
                  5 : [1,1,0,0],
                  6 : [0,1,1,0],
                  7 : [0,0,1,1] }

    cnt = 0
    time = 1
    stack = []
    while time != l + 1 :
        time += 1
        at = arr[r][c]
        # print(at)
        for l, ll in enumerate(pipe_rdlu[at]) :         # ll -> 뚫린 구멍 방향
            if ll :
                if ll == 0 :
                    cl = 2
                elif ll == 1 :
                    cl = 3
                elif ll == 2 :
                    cl = 0
                else :
                    cl = 1
                ar = r + rdlu[l][0]
                ac = c + rdlu[l][1]
                if 0 <= ar < n and 0 <= ac < m :        # 유효할때
                    if ll == pipe_rdlu[arr[ar][ac]][cl] :  # 파이프 연결 되어있으면
                        stack.append([[ar],[ac]])
            else :
                pass

