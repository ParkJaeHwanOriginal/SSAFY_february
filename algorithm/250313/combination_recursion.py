arr = ['a', 'b', 'c', 'd', 'e']
n = 3

path = []

# 5중 3
def recur(cnt, start) :
    # n 명이면 종료
    if cnt == n :
        print(*path)
        return

    # for i in range(이전에 뽑았던 인덱스 + 1부터, len(arr)) :
    # start : 이전 재귀로부터 넘겨받아야 하는 값
    for i in range(start, len(arr)) :
        path.append(arr[i])
        # i : i번째를 뽑겠다.
        # i + 1 을 매개변수로 전달, 다음 재귀부터는 i + 1 부터 고려
        recur(cnt + 1, i + 1)
        path.pop()

recur(0, 0)