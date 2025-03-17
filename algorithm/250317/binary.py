def binary(start, end, i, to = 'c') :
    mid = (start + end) // 2
    if start > end :
        return False
    if a_lst[mid] == i :
        return True
    if a_lst[mid] < i :
        if to == 'r' :
            return False
        return binary(mid+1, end, i, 'r')
    else :
        if to == 'l' :
            return False
        return binary(start, mid-1, i, 'l')

t = int(input())
for tc in range(1, t+1) :
    n, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    a_lst.sort()

    answer = 0
    for i in b_lst :
        if binary(0, n-1, i) :
            answer += 1
    print(f'#{tc} {answer}')