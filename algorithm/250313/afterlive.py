# # 부분집합
# N = 4
# friends = ['한놈', '두식이', '석삼', '너구리']
#
# # 2^4
# # p = [0, 0, 0, 0]
# # p = [0, 0, 0, 1]
# # ...
# # p = [1, 1, 1, 1]
#
# p = [-1] * N
# def recur(k) :
#     if k == N :                     # N과 같은 4, 4개의 길이를 다 맞췄다면
#         print(p)
#         for i in range(N) :
#             if p[i] :
#                 print(friends[i], end = ' ')
#         print()
#         return
#     for i in range(2) :             # 있냐 없냐의 0, 1을 리스트 p에 정리하는것
#         p[k] = i
#         recur(k+1)
# recur(0)
#
# # -----------------------------
# # 강사님 코드
# N = 4
# lst = ['프랑스', '영국', '태국', '미국']
#
# p = [-1] * N
# def recur(k, mid):
#     if k==N:
#         print(mid)
#         return
#
#     recur(k + 1, mid)
#
#     recur(k + 1, mid+[lst[k]])
#
# recur(0, [])

# 순열
N = 4
lst = ['프랑스', '영국', '태국', '미국']

M = 3

def perm(k) :
    if k == M :
        print(p)
        for i in range(M) :
            print(lst[p[i]], end = ' ')
        print()
        return

    for i in range(N) :
        if not used[i] :
            used[i] = True
            p[k] = i
            print(used, p)
            perm(k+1)
            used[i] = False

p = [-1] * M
used = [False] * N
perm(0)

# -----------------------
# 강사님 코드
# N = 4
# M = 3
# friends = ['A', 'B', 'C', 'D']
#
# def permu(k, mid):
#     if k==M:
#         print(p)
#         # for i in range(M):
#         #     print(friends[p[i]], end=' ')
#         # print()
#         print(mid)
#         return
#
#     for i in range(N):
#         if not used[i]:
#             used[i] = True
#             p[k] = i
#             permu(k+1, mid+[friends[i]])
#             used[i] = False
#
#
# used = [False] * N
# p = [-1]*M
# permu(0, [])

# 조합
# 이건 그냥 강사님꺼 코드 받아오자
N = 4
lst = ['프랑스', '영국', '태국', '미국']

M = 3
#
# p = [0, 1, 2]
# p = [0, 1, 3]
# p = [0, 2, 3]
# p = [3, 2, 1]

def comb(k, st, mid):
    if k==M:
        # print(p)
        # for i in range(M):
        #     print(lst[p[i]], end = ' ')
        # print()
        print(mid)
        return

    for i in range(st, N):
        p[k] = i
        comb(k+1, i+1, mid+[lst[i]])

p = [-1] * M
comb(0, 0, [])