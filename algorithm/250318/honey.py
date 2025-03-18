def subset(honey_lst, c) :
    n = len(honey_lst)
    subset_lst = []
    for i in range(1 << n) :
        num = 0
        subset = []
        for j in range(n) :
            if i & (1 << j) :
                if num + honey_lst[j] > c :
                    continue
                subset.append(honey_lst[j])
                num += honey_lst[j]
        subset_lst.append(subset)
    return subset_lst

def compare_honey(row, col, fir_ggul) :
    global answer
    ok = two_in_row
    for i in range(row+(int(two_in_row)+1)%2, n) :
        for j in range(int(ok) * (n + row), n-m+1) :
            sec_honey = arr[i][j:j+m]
            subset_lst = subset(sec_honey,c)
            sec_ggul = 0
            for tong in subset_lst :
                temp_ggul = 0
                for t in tong :
                    temp_ggul += t**2
                if temp_ggul > sec_ggul :
                    sec_ggul = temp_ggul
            if answer < fir_ggul + sec_ggul :
                answer = fir_ggul + sec_ggul
        ok = False



t = int(input())
for tc in range(1, t+1) :
    n, m, c = map(int, input().split())
    arr = [ list(map(int, input().split())) for _ in range(n) ]
    two_in_row = (n - m) >= m
    answer = 0
    for row in range(n) :
        for col in range(n-m+1) :
            fir_honey = arr[row][col:col+m]
            subset_lst = subset(fir_honey, c)
            fir_ggul = 0
            for tong in subset_lst :
                temp_ggul = 0
                for t in tong :
                    temp_ggul += t**2
                if temp_ggul > fir_ggul :
                    fir_ggul = temp_ggul
            # print(fir_ggul)
            # print('-----------')
            compare_honey(row, col, fir_ggul)

    print(f'#{tc} {answer}')
