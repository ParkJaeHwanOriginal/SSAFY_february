def combi(start, sum) :
    global gapsum
    if sum - b >= 0 :
        if gapsum > sum - b :
            gapsum = sum-b
        return gapsum

    for i in range(start, len(lst)) :
        combi(i+1, sum + lst[i])

t = int(input())
for tc in range(1, t+1) :
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))

    gapsum = sum(lst)
    combi(0, 0)
    print(f'#{tc} {gapsum}')