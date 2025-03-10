t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    while len(lst) > 1 :
        top = 0
        for i in range(len(lst)) :
            if lst[top] < lst[i] :
                top = i
        for i in lst[:top] :
            answer += lst[top]-i
        lst = lst[top+1:]
        # print(lst)
    print(f'#{tc} {answer}')