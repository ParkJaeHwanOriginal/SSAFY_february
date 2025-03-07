# tc = int(input())
# for ii in range(1, tc + 1) :
#     n = int(input())
#     arr = []
#     for ll in range(n) :
#         str = input()
#         lst = [ l for l in str ]
#         arr.append(lst)
#     rdlu = [[0,1],[1,0],[0,-1],[-1,0]]
#     answer = 0
#
#     for i in range(n) :
#         for j in range(n) :
#             cnt = 0
#             if arr[i][j] == 'C' :
#                 cnt = 3
#             elif arr[i][j] == 'B' :
#                 cnt = 2
#             elif arr[i][j] == 'A' :
#                 cnt = 1
#             for k in range(1, cnt + 1):
#                 for kk in rdlu:
#                     ni = i + (kk[0] * k)
#                     nj = j + (kk[1] * k)
#                     if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == "H":
#                         arr[ni][nj] = "X"
#     for i in range(n) :
#         for j in range(n) :
#             if arr[i][j] == "H" :
#                 answer += 1
#     print(f'#{ii} {answer}')

tc = int(input())
for i in range(1, tc + 1) :
    n = int(input())
    n_n = n
    nn = n_n // 2

    lv = 0
    while n >= 2 :
        n //= 2
        lv += 1

    lst = [0] * (n+1)
    for ll in range(lv, -1, -1) :
        a = 2**ll
        if a > n_n :
            a = n_n - 2**(ll-1)
        for l in range(2**ll) :
            po = 2**ll + l
            lst[po] = (l + l + 1) * (2**(lv-ll))
    # print(lst)
    print(f'#{i} {nn+1} {lst[nn]}')
