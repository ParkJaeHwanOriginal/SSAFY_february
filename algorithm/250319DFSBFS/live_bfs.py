import sys
sys.stdin = open('input.txt', 'r')

def bfs(node) :
    q = [node]    # 시작점을 넣은 상태로 출발

    # 1. 가장 앞에 있는 노드를 뽑는다
    # 2. 해당 노드에서 갈 수 있는 노드들을 queue에 넣는다
    while q :
        now = q.pop(0)
        print(now, end = ' ')
        # 인접한 노드들을 확인
        for next_node in graph[now] :
            if visited[next_node] :
                continue
            visited[next_node] = 1
            q.append(next_node)

N, M = map(int, input().split())
# 인접 리스트 (N * N ([]))
graph = [ [] for _ in range(N + 1) ]
visited = [0] * (N + 1)

for _ in range(M) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) # 양방향일때, 뒤집어서 저장해주기

visited[1] = 1 # 방문점 초기화
bfs(1)