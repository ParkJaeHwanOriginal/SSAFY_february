def solution(X, Y):
    answer = []
    x_cnt = [0] * 10
    y_cnt = [0] * 10

    for i in X :
        x_cnt[int(i)] += 1
    for i in Y :
        y_cnt[int(i)] += 1
    # print(x_cnt, y_cnt)
    for i in range(10) :
        cnt = min(x_cnt[i], y_cnt[i])
        for _ in range(cnt) :
            answer += repr(i)
    if not answer :
        answer.append(-1)
    answer = sorted(answer, reverse = True)
    answer = ' '.join(answer)
    return answer
solution("5525","1255")