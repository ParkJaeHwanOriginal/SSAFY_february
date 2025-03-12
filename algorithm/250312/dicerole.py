# 주사위 3개를 던져 합이 10 이하인 경우의 수는 몇개?
# 3번 던지고, 1 ~ 6 값을 갖는 주사위

path = []
result = 0

def recur(cnt, total) :
    global result
    # 이미 10을 넘긴 경우
    # 기저 조건에서 경우의 수 줄이기
    if total > 10 :
        return
    if cnt == 3 :
        if total <= 10 :
            result += 1
            print(path)
        return
    for num in range(1, 7) :
        path.append(num)
        recur(cnt + 1, total + num)
        path.pop()
recur(0,0)