import heapq
def dijkstra(start_node) :
    pq = [ (0, start_node) ]
    dists = [21e8] * (V + 1)
    dists[start_node] = 0

    while pq :
        weight, node = heapq.heappop(pq)
        if weight > dists[node] :
            continue
        for next_info in graph[node] :
            next_weight, next_node = next_info[0], next_info[1]
            new_weight = next_weight + weight
            if dists[next_node] <= new_weight :
                continue
            dists[next_node] = new_weight
            heapq.heappush(pq, (new_weight, next_node))
    return dists
t = int(input())
for tc in range(1, t+1) :
    V, E = map(int, input().split())
    graph = [ [] for i in range(V+1) ]
    for i in range(E) :
        start, end, weight = map(int, input().split())
        graph[start].append( (weight, end) )

    answer_lst = dijkstra(0)
    print(answer_lst)
    print(f'#{tc} {answer_lst[V]}')
