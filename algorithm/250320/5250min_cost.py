t = int(input())
for tc in range(1, t + 1) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    rd = [ [0,1], [1,1] ]
    graph = []
    for i in range(n) :
        graph.append([ [] for i in range(n) ])
    print(graph)
    for i in range(n) :
        for j in range(n) :
            