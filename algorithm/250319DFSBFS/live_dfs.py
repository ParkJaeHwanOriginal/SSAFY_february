import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
# 1. 그래프를 저장하기
# - 비어있는 그래프를 생성
# - 그래프 정보를 입력받아 넣기

def dfs(node) :
    # 보통의 그래프 문제들에서 종료 조건이 있을것이다
    # if 문으로 가지치기 or 종료 선언하기 :
    #     return

    print(node, end = " ")

    #  내가 갈 수 있는 후보들을 모두 확인하면서, 한 곳으로 진행
    for next_node in graph[node] :
        # 이미 방문했다면 가지 마라
        if visited[next_node] :
            continue
        visited[next_node] = 1
        dfs(next_node)

# 인접 행렬 (N * N 의 0 배열)
graph = [ [0] * N for _ in range(N + 1) ]
# 인접 리스트 (N * N ([]))
graph = [ [] for _ in range(N + 1) ]

for _ in range(M) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) # 양방향일때, 뒤집어서 저장해주기

visited = [0] * (N + 1)
visited[1] = 1 # 방문점 초기화
dfs(1)
print(graph)