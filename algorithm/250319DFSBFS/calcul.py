from collections import deque

def bfs(a, b) :
    visited = set([a])
    cnt = 0
    q = deque([(a, cnt)])
    while q :
        num, cnt = q.popleft()

        num_lst = [(num + 1), (num - 1), (num * 2), (num - 10)]
        if num > b :
            num_lst = [(num + 1), (num - 1), (num - 10)]

        cnt += 1
        for i in num_lst :
            if i == b :
                return cnt
            if i > 1000000 or i <= 0 :
                continue
            if i not in visited :
                q.append((i,cnt))
                visited.add(i)

t = int(input())
for tc in range(1, t+1) :
    a, b = map(int, input().split())

    cnt = bfs(a, b)
    print(f'#{tc} {cnt}')
    print(f'#{tc} {cnt}')
