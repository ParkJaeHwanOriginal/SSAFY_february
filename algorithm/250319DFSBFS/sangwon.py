import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1) :
    n, m = map(int, input().split())
    parents = [ [] for _ in range(n+1) ]
    for i in range(m) :
        x, y = sorted(map(int, input().split()))
        parents[y] += [x]
        parents[x] += [y]
    answer = []
    answer += parents[1]
    for i in parents[1] :
        answer += parents[i]
    answer = len(set(answer))
    if answer != 0 :
        answer -= 1
    print(f'#{tc} {answer}')