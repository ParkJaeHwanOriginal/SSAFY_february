import sys
sys.stdin = open('input.txt','r')

t = int(input())
for tc in range(1, t+1) :
    n, m = map(int, input().split())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    around = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    answer = 0
    for i in range(n) :
        for j in range(m) :
            temp = 0
            for k in around :
                if 0 <= (i + k[0]) < n and 0 <= (j + k[1]) < m :
                    if arr[i][j] > arr[i+k[0]][j+k[1]] :
                        temp += 1
            if temp > 3 :
                answer += 1
    print(f'#{tc} {answer}')