t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    rail = [0] * 401
    for l in range(n) :
        start, end = sorted(list(map(int, input().split())))
        if start % 2 == 0 :
            start -= 1
        if end % 2 == 1 :
            end += 1
        for ll in range(start, end+1) :
            rail[ll] += 1
    print(f'#{tc} {max(rail)}')
