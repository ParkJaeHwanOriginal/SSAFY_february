def solution(n, m) :
    mask = (1<<n) - 1
    if m & mask == mask :
        return "ON"
    return "OFF"

tc = int(input())
for i in range(1, tc+1) :
    n, m = map(int, input().split())
    print(f'#{i} {solution(n, m)}')
