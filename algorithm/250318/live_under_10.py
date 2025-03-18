set = set(i for i in range(1, 11))
print(set)
visited = [0] * (len(set)+1)

def subset(set, lst = []) :
    if sum(lst) == 10 :
        print(lst)
        return
    for i in set :
        if visited[i] == 0 :
            visited[i] = 1
            subset(set, lst + [i])
            visited[i] = 0

subset(set)