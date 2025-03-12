# 숫자 3개가 연속되었는가
# 숫자 3개가 같은가

used = [0] * 6
path = []

def is_baby_gin() :
    cnt = 0
    for i in range(4) :
        if path[i] == path[i+1] == path[i+2] :
            cnt += 1
        if path[i] == path[i+1] - 1 == path[i+2] - 2 :
            cnt += 1
    if cnt == 2 :
        return True

def recur(cnt) :
    if cnt == 6 :
        print(path)
        return

    for idx in range(6) :
        if used[idx] :
            continue
        used[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        used[idx] = 0


arr = list(map(int, input().split()))
recur(0)