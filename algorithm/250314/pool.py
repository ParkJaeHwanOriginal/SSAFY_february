import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1) :
    day, month, thr_month, year = map(int, input().split())
    lst = list(map(int,input().split()))

    # 일권 비용으로 변경
    for i in range(len(lst)) :
        if lst[i] * day > month :
            lst[i] = month
        else :
            lst[i] *= day
    print(lst)

    answer = 0
    for i in range(len(lst)) :
        if i == 1 or i == 2 :                                       # 월요금만 더하는 answer와 3달요금을 계산해준 answer를 나눠서 비교하면서 가야할 듯
            answer += lst[i]

        elif i >= 3 :
            if answer - (lst[i-2] + lst[i-1]) + month > answer + lst[i] : # 앞전 2달을 포함한 3개월을 3달요금으로 내는게 각달요금보다 싸다면
                answer = answer - lst[i-2] - lst[i-1] + month
            else :
                answer += thr_month
    print(answer)

