# def combi(m, start = 0, lst = []) :
#     if m == 0 :
#         selected_lst.append(lst)
#     for i in range(start, len(chicken_lst)) :
#         combi(m-1, i + 1, lst + [chicken_lst[i]])
#
# n, m = map(int, input().split())
# arr = [ list(map(int, input().split())) for _ in range(n) ]
# chicken_lst = []
# home_lst = []
# for i in range(n) :
#     for j in range(n) :
#         if arr[i][j] == 1 :
#             home_lst.append((i,j))
#         elif arr[i][j] == 2 :
#             chicken_lst.append((i,j))
# selected_lst = []
# combi(m)
#
# answer = ((2*n)-1)*len(home_lst)
# for i in selected_lst :
#     temp_dist = 0
#     for j in home_lst :
#         # 특정 집 j에 대한 '선택 된 치킨집들' 중 가장 가까운 치킨거리
#         dist = 2*n-1
#         for ii in i :
#             ii_dist = abs(j[0] - ii[0]) + abs(j[1] - ii[1])
#             if ii_dist < dist :
#                 dist = ii_dist
#         temp_dist += dist
#         if temp_dist > answer :
#             continue
#     if temp_dist < answer :
#         answer = temp_dist
# print(answer)

# --------------------------

def combi(m, start = 0, lst = []) :
    global answer
    if m == 0 :
        temp_dist = 0
        for i in home_lst :
            temp = 2*n - 1
            for j in lst :
                dist = abs(j[0] - i[0]) + abs(j[1] - i[1])
                if dist < temp :
                    temp = dist
            temp_dist += temp
        if answer > temp_dist :
            answer = temp_dist

    for i in range(start, len(chicken_lst)) :
        combi(m-1, i + 1, lst + [chicken_lst[i]])

n, m = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(n) ]
chicken_lst = []
home_lst = []
answer = ((2*n)-1)*len(home_lst)
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 :
            home_lst.append((i,j))
        elif arr[i][j] == 2 :
            chicken_lst.append((i,j))
selected_lst = []
combi(m)
print(answer)