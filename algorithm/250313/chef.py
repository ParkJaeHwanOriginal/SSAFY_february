import sys
sys.stdin = open('input.txt', 'r')

def combi(k, start, mid) :
    if k == n/2 :
        food_lst.append(mid)
        return
    for i in range(start+1, n+1) :
        combi(k+1, i, mid + [i])

t = int(input())
for tc in range(1, 1 + t) :
    n = int(input())
    arr = [ list(map(int, input().split())) for _ in range(n) ]

    food_lst = []
    combi(1, 1, [1])
    # print(food_lst, len(food_lst))
    for i in food_lst :
        food = [ i for i in range(1, n+1) ]
        for ii in i[::-1] :
            food.pop(ii-1)
        print(food_lst, food)
