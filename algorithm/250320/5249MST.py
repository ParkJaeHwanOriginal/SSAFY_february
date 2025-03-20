# import heapq
#
# def prim(node) :
#     pq = [ (0, node) ]
#     MST = [0] * (V + 1)
#     min_weight = 0
#     while pq :
#         weight, node = heapq.heappop(pq)
#         if MST[node] :
#             continue
#         MST[node] = 1
#         min_weight += weight
#
#         for i in range(V+1) :
#             if MST[i] : continue
#             if not graph[node][i] : continue
#             heapq.heappush(pq, (graph[node][i], i))
#     return min_weight

def findset(x) :
    if parents[x] == x :
        return x
    parents[x] = findset(parents[x])
    return parents[x]
def union(x, y) :
    ref_x = findset(x)
    ref_y = findset(y)

    if ref_x == ref_y :
        return
    if ref_x < ref_y :
        parents[ref_y] = ref_x
    else :
        parents[ref_x] = ref_y

t = int(input())
for tc in range(1, t+1) :
    V, E = map(int, input().split())
#     graph = [ [0] * (V + 1) for _ in range(V + 1) ]
#
#     for i in range(E) :
#         start, end, weight = map(int, input().split())
#         graph[start][end] = weight
#         graph[end][start] = weight
#
#     print(f'#{tc} {prim(0)}')

    edges = []
    for i in range(E) :
        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))
    edges.sort(key=lambda x : x[2]) # 가중치로 오름정렬
    parents = [ i for i in range(V+1) ]
    cnt = 0
    answer = 0
    for start, end, weight in edges :
        if findset(start) == findset(end) :
            continue
        union(start, end)
        cnt += 1
        answer += weight
        if cnt == V :
            break
    print(f'#{tc} {answer}')