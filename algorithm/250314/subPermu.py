import sys
sys.stdin = open('input.txt', 'r')

def combi(start, sum) :
    global cnt
    if sum > k :
        return
    if sum == k :
        cnt += 1
        return
    for i in range(start, len(lst)) :
        combi(i+1, sum + lst[i])

t = int(input())
for tc in range(1, t+1) :
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    combi(0, 0)
    print(f'#{tc} {cnt}')