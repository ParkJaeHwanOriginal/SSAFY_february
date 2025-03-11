import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    stop = [0] * 1001
    for l in range(n) :
        k, start, end = map(int, input().split())
        if k == 1 :
            for i in range(start, end+1) :
                stop[i] += 1
        elif k == 2 :
            for i in range(start, end, 2) :
                stop[i] += 1
            stop[end] += 1
        else :
            if start % 2 == 0 :
                for i in range(start, end) :
                    if i % 4 == 0 :
                        stop[i] += 1
                if start % 4 != 0 :
                    stop[start] += 1
                stop[end] += 1
            else :
                for i in range(start, end) :
                    if i % 3 == 0 and i % 10 != 0 :
                        stop[i] += 1
                if start % 3 != 0 :
                    stop[start] += 1
                stop[end] += 1
    print(f'#{tc} {max(stop)}')