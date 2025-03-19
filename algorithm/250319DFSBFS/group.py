def dfs(i) :
    if visited[i] == 1 :
        return
    visited[i] = 1
    for next_node in graph[i] :
        if visited[next_node] :
            continue
        dfs(next_node)

t = int(input())
for tc in range(1, t+1) :
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    graph = [ [] for _ in range(n+1) ]
    for i in range(m) :
        s, e = lst[i*2], lst[i*2+1]
        graph[s].append(e)
        graph[e].append(s)
    visited = [0] * (n+1)
    answer = 0
    for i in range(1, n+1) :
        if visited[i] :
            continue
        dfs(i)
        answer += 1
    print(f'#{tc} {answer}')
