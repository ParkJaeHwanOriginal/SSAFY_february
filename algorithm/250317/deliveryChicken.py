n, m = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(n) ]
chicken_lst = []
home_lst = []
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 :
            home_lst.append((i,j))
        elif arr[i][j] == 2 :
            chicken_lst.append((i,j))
winner_chicken = [0] * len(chicken_lst)
for i in home_lst :
    temp_dist = []
    for ii in chicken_lst :
        dist = abs(ii[0]-i[0]) + abs(ii[1]-i[1])
        temp_dist.append(dist)
    # print(temp_dist)
    for iii in range(len(temp_dist)):
        if temp_dist[iii] == min(temp_dist) :
            winner_chicken[iii] += 1
print(winner_chicken)

winner_chicken_lst = []
winner = dict()
while len(winner_chicken_lst) != m :
    for i in range(len(winner_chicken)-1, -1, -1) :
        if winner_chicken[i] == max(winner_chicken) :
            winner_chicken_lst.append(chicken_lst[i])
            winner_chicken.pop(i)
        if len(winner_chicken_lst) == m :
            break
print(winner_chicken_lst)
