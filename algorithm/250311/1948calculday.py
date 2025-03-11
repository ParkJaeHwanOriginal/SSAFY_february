month_day_dict = { 1 : 31,
                   2 : 28,
                   3 : 31,
                   4 : 30,
                   5 : 31,
                   6 : 30,
                   7 : 31,
                   8 : 31,
                   9 : 30,
                   10 : 31,
                   11 : 30,
                   12 : 31 }

t = int(input())
for tc in range(1, t+1) :
    sm, sd, em, ed = map(int, input().split())
    answer = 0
    if sm == em :
        answer = ed - sd + 1
    else :
        if em - sm > 1 : # 2달 이상 차이
            for i in range(sm + 1, em) :
                answer += month_day_dict[i]
        answer += month_day_dict[sm] - sd + 1
        answer += ed
    print(f'#{tc} {answer}')