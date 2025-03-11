from collections import deque

n = int(input())
adj_lst = [ [] for i in range(n+1) ]

for i in range(n-1) :
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

queue = deque([1])
parent_lst = [0] * (n+1)
visited = [0] * (n+1)
while queue :
    parent = queue.popleft()
    if visited[parent] == 0 :
        visited[parent] = 1

    for l in adj_lst[parent] :
        if visited[l] == 0 :    # l 이 자식노드라는 뜻
            queue.append(l)
            parent_lst[l] = parent
        else :                  # 가본적 있다는 것은 부모노드라는 뜻
            pass

for i in parent_lst[2:] :
    print(i)