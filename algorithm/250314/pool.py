import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1) :
    day, month, thr_month, year = map(int, input().split())
    lst = list(map(int,input().split()))
    answer = 0
    for i in range(len(lst)) :                  # 일권 or 월권
        if lst[i] * 10 > month :
            lst[i] = month
            answer += month
        else :
            answer += 10 * lst[i]
    print(answer)

    if year < answer :                          # 모두 연권으로
        answer = year

    # temp_answer = 0
    # for i in range(len(lst)) :
    #     if i < 10 :
    #         if
    # for i in lst :
    #     if i*10 > month :
    #         temp_answer += month
    #     else :
    #         temp_answer += i*10
    # if temp_answer < answer :
    #     answer = temp_answer

    print(answer)